"""This module contains the IntentRecognitionStrategy class and its subclasses
"""
import json
import logging
from .openai_api import generate_responses
from converso.AI.intentions_entities import intentions


def check_treshold(intention_object):
    """Checks if the confidence is above the treshold.
    :param intention_object: float: The confidence of the intent recognition.
    :return: bool: True if the confidence is above the treshold, False otherwise.
    """
    treshold = 0.8
    if intention_object["confidence"] >= treshold:
        return intention_object
    else:
        return {"intention": "nothing_related", "confidence": intention_object["confidence"]}


class IntentRecognitionStrategy:
    """Abstract class for recognizing the intent of the user's message."""
    def recognize_intent(self, prompt):
        """Recognizes the intent of the user's message.
        :param prompt: str: The user's message.
        :return: str: The intent of the user's message.
        """
        pass


class OpenAIIntentRecognition(IntentRecognitionStrategy):
    """Class for recognizing the intent of the user's message using OpenAI's GPT-3 API."""
    def recognize_intent(self, prompt):
        """Recognizes the intent of the user's message.
        :param prompt: str: The user's message.
        :return: str: The intent of the user's message.
        """
        prompt = f"""user_prompt: "{prompt}" from this intentions: {str(intentions)} tell 
        me the intention you found in the user_prompt and your confidence.answer me with a json like this just the 
        json nothing more {{\n"intention": "change_nib",\n"confidence": 0.89\n}} and if the intention is absurd then
        use the intention nothing_related."""

        logging.info("Recognizing intent for user prompt")
        intention_recognition_response = generate_responses(prompt)
        intention_recognition_object = check_treshold(json.loads(intention_recognition_response))
        logging.info("Recognized intent: %s", intention_recognition_object["intention"])
        return intention_recognition_object


class DistilBERTIntentRecognition(IntentRecognitionStrategy):
    """Class for recognizing the intent of the user's message using our own fine-tuned pre-trained model DistilBERT."""
    def recognize_intent(self, prompt):
        """Recognizes the intent of the user's message.
        :param prompt: str: The user's message.
        :return: str: The intent of the user's message.
        """
        # Use Spacy's NER to extract named entities from the text
        pass
