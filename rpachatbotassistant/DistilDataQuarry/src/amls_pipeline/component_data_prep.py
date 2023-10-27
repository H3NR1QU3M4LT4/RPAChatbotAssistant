""" This module contains the code for creating the data prep component
"""
from azure.ai.ml import command
from azure.ai.ml import Input, Output


def create_data_prep_component(ml_client, data_prep_src_dir, pipeline_job_env):
    """ Creates the data prep component.
    @param ml_client: The ml client.
    @param data_prep_src_dir: The data prep source directory.
    @param pipeline_job_env: The pipeline job environment.
    @return: The data prep component.
    """
    print(f"Creating data prep component...")
    data_prep_component = command(
        name="data_prep_bert_intentions",
        display_name="Data preparation for training",
        description="reads a csv input, split the input to train and test",
        inputs={
            "data": Input(type="uri_folder"),
            "test_size": Input(type="number"),
            "val_size": Input(type="number"),
            "tokenizer": Input(type="string"),
        },
        outputs=dict(
            encoded_dataset=Output(type="uri_folder", mode="rw_mount"),
            labels=Output(type="uri_folder", mode="rw_mount"),
            labels2id=Output(type="uri_folder", mode="rw_mount"),
            id2label=Output(type="uri_folder", mode="rw_mount"),
        ),
        # The source folder of the component
        code=data_prep_src_dir,
        command="""python data_prep.py \
                --data ${{inputs.data}} --test_size ${{inputs.test_size}} \
                --val_size ${{inputs.val_size}} \
                --tokenizer ${{inputs.tokenizer}} \
                --encoded_dataset ${{outputs.encoded_dataset}} \
                --labels ${{outputs.labels}} \
                --labels2id ${{outputs.labels2id}} \
                --id2label ${{outputs.id2label}} \
                """,
        environment=f"{pipeline_job_env.name}:{pipeline_job_env.version}",
    )

    # Now we register the component to the workspace
    data_prep_component = ml_client.create_or_update(data_prep_component.component)

    # Create (register) the component in your workspace
    print(
        f"Component {data_prep_component.name} with Version {data_prep_component.version} is registered"
    )

    return data_prep_component
