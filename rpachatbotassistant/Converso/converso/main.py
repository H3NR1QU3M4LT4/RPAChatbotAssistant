"""Python Library to generate responses using OpenAI's GPT-3 API and
detect intents and entities using our own fine-tuned pre-trained model DistilBERT.
"""
import os
from converso.converso_factory import ChatbotFactory
from converso.chatbot_strategy import chatbot_strategy_handler
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(name)s %(filename)s:%(lineno)d %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)


def check_openai_api_key():
    """ Checks if the environment variables are set.
    :return: None
    """
    if os.getenv('OPENAI_API_KEY') is None:
        raise Exception("Please set the OPENAI_API_KEY environment variable.")
    elif os.getenv('OPENAI_API_TYPE') is None:
        raise Exception("Please set the OPENAI_API_TYPE environment variable.")
    elif os.getenv('OPENAI_API_BASE') is None:
        raise Exception("Please set the OPENAI_API_BASE environment variable.")
    elif os.getenv('OPENAI_API_API_VERSION') is None:
        raise Exception("Please set the OPENAI_API_API_VERSION environment variable.")


def converso(prompt: str) -> str:
    """ Runs name_entity_recognition, intent_recognition and send_information_rpa and after get
    the response from RPA, it will send the response to the user using the generate_response function.
    :param prompt: str: The prompt to be sent to the user.
    :return: str: The response from the OpenAIGPTGenerator based on response from RPA.
    """
    check_openai_api_key()
    factory = ChatbotFactory("openai", "openai", "openai", "http")
    ner = factory.create_ner()
    intent_recognizer = factory.create_intent_recognition()
    response_generator = factory.create_response_generator()
    rpa_service = factory.create_send_information_rpa()

    intent = intent_recognizer.recognize_intent(prompt)
    response = chatbot_strategy_handler(intent, prompt, response_generator, ner, rpa_service)

    return response

"""
# find in the folder all txt files
txt_files = []
for file in os.listdir("C:/Users/steixe01/AzureDevopsRepos/RPAChatbotAssistant/rpachatbotassistant/Converso/converso"):
    if file.endswith(".txt"):
        txt_files.append(file)

# READ THE TXT FILES AND RUN THE CONVERSO FUNCTION
for file in txt_files:
    with open(file, 'r') as f:
        for line in f:
            ola = converso(line)
            print(ola)
            print("»»»»»»»»»»»»»»»»»»»»»»««««««««««««««««««««")
"""
