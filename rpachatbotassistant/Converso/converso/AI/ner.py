"""This module contains the NER strategies to extract entities from the user's input.
"""
import json
import logging
from .openai_api import generate_responses
from converso.AI.intentions_entities import entities


def check_treshold(ner_object):
    """Checks if the confidence is above the treshold.
    :param ner_object: float: The confidence of the ner recognition.
    :return: bool: True if the confidence is above the treshold, False otherwise.
    """
    treshold = 0.8
    entities_high_treshold = {}
    for entity, details in ner_object["entities"].items():
        if details["confidence"] >= treshold:
            entities_high_treshold[entity] = details
    return {"entities": entities_high_treshold}


class NERStrategy:
    """Abstract class for extracting entities from the user's input.
    :param prompt: str: The user's input.
    :return: str: The entities extracted from the user's input.
    """
    def extract_entities(self, prompt):
        pass


class OpenAINER(NERStrategy):
    """Class for extracting entities from the user's input using OpenAI's GPT-3 API."""
    def extract_entities(self, prompt):
        """Extracts entities from the user's input.
        :param prompt: str: The user's input.
        :return: str: The entities extracted from the user's input.
        """
        prompt = f"""user_prompt: "{prompt}"\n\nfrom this entities and only this entities use them as they are (dont 
        create new ones or add new ones):
         {str(entities)} tell  me the entities you found in the user_prompt and your confidence.\nanswer me with 
         a json like this just the json nothing more, notice that entities NEEDS to be an object and never a list, 
         always an object composed by objects like e.g.:
        \n{{\n"entities": {{{{"date": {{value": "12-10-2022", "confidence": 0.89}}}},{{{{"office": {{"value": "Porto", 
        "confidence": 0.89}}}}, {{{{"parking_lot": {{"value":"2a", "confidence": 0.89}}}}}},\n\n}}"""

        logging.info("Recognizing entities for user prompt")
        name_entity_recognition_response = generate_responses(prompt)
        name_entity_recognition_object = check_treshold(json.loads(name_entity_recognition_response))
        logging.info("Recognized entities: %s", name_entity_recognition_object["entities"])
        return name_entity_recognition_object


class DistilBERTNER(NERStrategy):
    """Class for extracting entities from the user's input using our own fine-tuned pre-trained model DistilBERT."""
    def extract_entities(self, prompt):
        """Extracts entities from the user's input.
        :param prompt: str: The user's input.
        :return: str: The entities extracted from the user's input.
        """
        # Use Spacy's NER to extract named entities from the text
        pass


class SpacyNER(NERStrategy):
    """Class for extracting entities from the user's input using Spacy's NER."""
    def extract_entities(self, prompt):
        """Extracts entities from the user's input.
        :param prompt: str: The user's input.
        :return: str: The entities extracted from the user's input.
        """
        # Use Spacy's NER to extract named entities from the text
        pass
