"""Converso factory module that creates the different components of the chatbot.
"""
from converso.AI.ner import OpenAINER, SpacyNER, DistilBERTNER
from converso.AI.intent_recognition import OpenAIIntentRecognition, DistilBERTIntentRecognition
from converso.AI.generator import OpenAIGPTGenerator
from .SendInformationRPAStrategy import HttpSendInformationRPAStrategy


class ChatbotFactory:
    """Factory class for creating the different components of the chatbot."""
    def __init__(self, ner_type, intent_type, generator_type, rpa_type):
        """Initializes the ChatbotFactory class.
        :param ner_type: str: The type of NER to use.
        :param intent_type: str: The type of intent recognition to use."
        :param generator_type: str: The type of response generator to use.
        :param rpa_type: str: The type of RPA to use.
        """
        self.ner_type = ner_type
        self.intent_type = intent_type
        self.generator_type = generator_type
        self.rpa_type = rpa_type

    def create_ner(self):
        """Creates the NER object.
        :return: NER: The NER object.
        """
        if self.ner_type == "openai":
            return OpenAINER()
        elif self.ner_type == "spacy":
            return SpacyNER()
        elif self.ner_type == "distilbert":
            return DistilBERTNER()
        else:
            raise ValueError("Unsupported NER type")

    def create_intent_recognition(self):
        """Creates the intent recognition object.
        :return: IntentRecognition: The intent recognition object.
        """
        if self.intent_type == "openai":
            return OpenAIIntentRecognition()
        elif self.intent_type == "distil-bert":
            return DistilBERTIntentRecognition()
        else:
            raise ValueError("Unsupported intent recognition type")

    def create_response_generator(self):
        """Creates the response generator object.
        :return: ResponseGenerator: The response generator object.
        """
        if self.generator_type == "openai":
            return OpenAIGPTGenerator()
        else:
            raise ValueError("Unsupported response generator type")

    def create_send_information_rpa(self):
        """Creates to send information rpa object.
        :return: SendInformationRPA: to send information rpa object.
        """
        if self.rpa_type == "http":
            return HttpSendInformationRPAStrategy()
        else:
            raise ValueError("Unsupported send information rpa type")
