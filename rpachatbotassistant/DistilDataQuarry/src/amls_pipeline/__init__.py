""" Defines the pipeline for the Azure ML Studio project.
"""
from azure.ai.ml import dsl, Input

from src.amls_pipeline.component_data_prep import create_data_prep_component
from src.amls_pipeline.component_train import create_train_component


def mount_run_pipeline(cfg, original_dir, azure_credential, text_bert_intentions, cpu_cluster, pipeline_env):
    """ Sets up the pipeline for the Azure ML Studio project.
    @param cfg: The hydra configuration file.
    @param original_dir: The original directory of the project.
    @param azure_credential: The azure credential.
    @param text_bert_intentions: The text bert intentions dataset.
    @param cpu_cluster: The cpu cluster.
    @param pipeline_env: The pipeline environment.
    """
    print(f"Setting up pipeline...")
    data_prep_component = create_data_prep_component(azure_credential.ml_client,
                                                     f"{original_dir}/{cfg.data_prep_component.src_dir}",
                                                     pipeline_env)

    train_component = create_train_component(azure_credential.ml_client,
                                             f"{original_dir}/{cfg.train_component.src_dir}",
                                             pipeline_env)

    @dsl.pipeline(
        name=cfg.pipeline.name,
        compute=cpu_cluster.name,
        description=cfg.pipeline.description,
    )
    def bert_intentions_pipeline(
            pipeline_job_data_input,
            pipeline_job_test_size,
            pipeline_job_val_size,
            pipeline_job_tokenizer,
            pipeline_job_train_batch_size,
            pipeline_job_eval_batch_size,
            pipeline_job_num_train_epochs,
            pipeline_job_learning_rate,
            pipeline_job_registered_model_name,
            pipeline_job_model_name
    ):
        data_prep_job = data_prep_component(
            data=pipeline_job_data_input,
            test_size=pipeline_job_test_size,
            val_size=pipeline_job_val_size,
            tokenizer=pipeline_job_tokenizer

        )

        train_job = train_component(
            dataset=data_prep_job.outputs.encoded_dataset,
            labels=data_prep_job.outputs.labels,
            labels2id=data_prep_job.outputs.labels2id,
            id2label=data_prep_job.outputs.id2label,
            train_batch_size=pipeline_job_train_batch_size,
            eval_batch_size=pipeline_job_eval_batch_size,
            num_train_epochs=pipeline_job_num_train_epochs,
            learning_rate=pipeline_job_learning_rate,
            registered_model_name=pipeline_job_registered_model_name,
            model_name=pipeline_job_model_name
        )

        return {
            "pipeline_job_model": train_job.outputs.model,
        }

    pipeline = bert_intentions_pipeline(
        pipeline_job_data_input=Input(type="uri_file", path=text_bert_intentions.path),
        pipeline_job_test_size=cfg.data_prep_component.test_size,
        pipeline_job_val_size=cfg.data_prep_component.val_size,
        pipeline_job_tokenizer=cfg.data_prep_component.tokenizer,
        pipeline_job_train_batch_size=cfg.train_component.train_batch_size,
        pipeline_job_eval_batch_size=cfg.train_component.eval_batch_size,
        pipeline_job_num_train_epochs=cfg.train_component.num_train_epochs,
        pipeline_job_learning_rate=cfg.train_component.learning_rate,
        pipeline_job_registered_model_name=cfg.train_component.registered_model_name,
        pipeline_job_model_name=cfg.train_component.model_name
    )

    pipeline_job = azure_credential.ml_client.jobs.create_or_update(
        pipeline,
        experiment_name=cfg.experiment.name
    )

    azure_credential.ml_client.jobs.stream(pipeline_job.name)
