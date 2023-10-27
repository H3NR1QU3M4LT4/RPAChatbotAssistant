# RPAChatbotAssistant

The RPAChatbotAssistant is a Python-based chatbot assistant that is capable of automating a variety of tasks by integrating with different tools. Some of the tasks it can automate include changing NIB in Workday, requesting reports, booking tables and parking spaces in Merkle Offices, and approving travel requests in Travel Desk. The assistant's user interface is built using Streamlit, and its natural language processing capabilities are enhanced through the use of a fine-tuned DistilBERT model for intent classification and named entity recognition.

Each different project has its own README.md that explains what was done.

# Table of Contents
- [Get Started](#get-started)
  - [Git](#git)
  - [Installation](#installation)
  - [Dependencies](#dependencies)
- [ChattyStreamUI](#chattystreamui)
- [Converso](#converso)
- [DistilDataQuarry](#distildataquarry)
- [RPASimulator](#rpasimulator)
- [Conclusion](#conclusion)

# Get Started


## Git
To get started with the RPAChatbotAssistant, you can clone the repository using the following command:
* `git clone`

If you would like to contribute to the project, you can create a new branch with the following commands:
* `git checkout -b <branch-name>`
* `git add .`
* `git commit -m "<message>"`
* `git push`


## Installation
Before running the chatbot, you will need to install the required dependencies. To get started, follow these steps:

* Install Anaconda: https://docs.anaconda.com/anaconda/install/
* Create a new conda environment using the following command:
    * `conda create --name RPAChatBotAssistant python=3.9.16`
    * or `conda env create -f environment.yml`
* Activate the conda environment: `conda activate RPAChatBotAssistant`
* Export the conda environment to a YAML file: 
    * `conda env export | grep -v "^prefix: " > environment.yml` 
    * or `conda env export > environment.yml`
* Install poetry using the following command: `conda install -c conda-forge poetry`

For personalise UI:
* Install the required chatUI package and make any necessary changes by following these steps:
    * mkdir packages and cd packages
    * git clone https://github.com/AI-Yash/st-chat.git
    * cd packages/st-chat/
    * python setup.py install

If you want to change the chatUI frontend, install NodeJS (https://nodejs.org/en) and follow these steps:
* cd packages/st-chat/streamlit_chat/frontend
* npm install
* npm run build
* Reinstall setup.py.


## Dependencies
To install the required dependencies, run the following command:
* `poetry install`

If you would like to start from scratch, you can initialize a new Poetry project and add the required packages manually:
* `poetry init`
* `poetry add <packages>`

# ChattyStreamUI
To run the RPAChatbotAssistant, follow these steps:

Start the Streamlit server:
streamlit run main.py
or poetry run streamlit run main.py
Choose the desired tool from the list of available options.
Interact with the chatbot by entering text into the input field and pressing "Enter".

# Converso
* `streamlit run main.py` or `poetry run streamlit run main.py`

# DistilDataQuarry
## Fine-tuning DistilBERT Model
The chatbot's natural language processing capabilities are enhanced through the use of a fine-tuned DistilBERT model for intent classification and named entity recognition. If you would like to fine-tune the model further, you can do so by following these steps:

Prepare your dataset and split it into training and testing sets.
Fine-tune the DistilBERT model using the run_language_modeling.py script provided by the Hugging Face Transformers library.
Save the fine-tuned model to a file.
Update the chatbot's code to use the new model file.

# RPASimulator


# Conclusion
In conclusion, the RPAChatbotAssistant is a powerful tool that can streamline various tasks, saving time and increasing productivity. With its natural language processing capabilities, it can understand user intent and respond accordingly, making it easy to use for anyone. Additionally, the ability to fine-tune the DistilBERT model further enhances the chatbot's capabilities. By following the instructions in this README, you can get started with the RPAChatbotAssistant and even contribute to its development.