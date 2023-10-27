""" This is the main file to run the pipeline
"""
# If you want to run this file from the command line or Vs Code, you need to add the path to the root of the project
# import sys
# print(sys.path)
# change the path to the root of the project
# sys.path.append("/Users/steixe01/AzureDevopsRepos/RPAChatbotAssistant/rpachatbotassistant/DistilDataQuarry/")


import hydra
from omegaconf import DictConfig
from src.amls_pipeline import mount_run_pipeline
from azureml_infra_tools import setup_infrastructure
from dotenv import load_dotenv

load_dotenv()


@hydra.main(version_base="1.2", config_path="conf", config_name="config")
def main(cfg: DictConfig):
    """ Main function to run the pipeline
    @param cfg: hydra configuration file
    """
    # get original directory of the root of the project
    original_dir = hydra.utils.get_original_cwd()

    # create o setup with environment to run pipeline, client, cluster and data
    azure_credential, text_bert_intentions, cpu_cluster, pipeline_env = setup_infrastructure(cfg, original_dir)

    # create pipeline and run it
    mount_run_pipeline(cfg, original_dir, azure_credential, text_bert_intentions, cpu_cluster, pipeline_env)

    # deploy model to real time endpoint
    # deploy_model_to_endpoint(cfg, azure_credential)


if __name__ == "__main__":
    main()
