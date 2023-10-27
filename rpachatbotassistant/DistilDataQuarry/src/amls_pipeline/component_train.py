""" This module contains the code for creating the data train component
"""
from azure.ai.ml import command
from azure.ai.ml import Input, Output


def create_train_component(ml_client, train_src_dir, pipeline_job_env):
    """ Creates the train prep component.
    @param ml_client: The ml client.
    @param train_src_dir: The data prep source directory.
    @param pipeline_job_env: The pipeline job environment.
    @return: The data prep component.
    """
    print(f"Creating data prep component...")
    train_component = command(
        name="train_bert_intentions",
        display_name="Train bert intentions",
        description="reads a dataset with load_dataset and train a model",
        inputs={
            "dataset": Input(type="uri_folder"),
            "labels": Input(type="uri_folder"),
            "labels2id": Input(type="uri_folder"),
            "id2label": Input(type="uri_folder"),
            "train_batch_size": Input(type="number"),
            "eval_batch_size": Input(type="number"),
            "num_train_epochs": Input(type="number"),
            "learning_rate": Input(type="number"),
            "registered_model_name": Input(type="string"),
            "model_name": Input(type="string"),
        },
        outputs=dict(
            model=Output(type="uri_folder", mode="rw_mount"),
        ),
        # The source folder of the component
        code=train_src_dir,
        command="""python train.py \
                --dataset ${{inputs.dataset}} --labels ${{inputs.labels}} \
                --labels2id ${{inputs.labels2id}} --id2label ${{inputs.id2label}} \
                --train_batch_size ${{inputs.train_batch_size}} \
                --eval_batch_size ${{inputs.eval_batch_size}} \
                --num_train_epochs ${{inputs.num_train_epochs}} \
                --learning_rate ${{inputs.learning_rate}} \
                --registered_model_name ${{inputs.registered_model_name}} \
                --model_name ${{inputs.model_name}} \
                --model ${{outputs.model}} \
                """,
        environment=f"{pipeline_job_env.name}:{pipeline_job_env.version}",
    )

    # Now we register the component to the workspace
    train_component = ml_client.create_or_update(train_component.component)

    # Create (register) the component in your workspace
    print(
        f"Component {train_component.name} with Version {train_component.version} is registered"
    )

    return train_component
