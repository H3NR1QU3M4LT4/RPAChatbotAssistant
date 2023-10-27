"""This module contains the class for generating responses from the chatbot.
"""
import logging
from .openai_api import generate_responses


class ChatGenerator:
    """Abstract class for generating responses from the chatbot."""
    def respond(self, prompt):
        """Generates a response to the given prompt.
        :param prompt: str: The prompt to be sent to the user.
        :return: str: The response from the chatbot.
        """
        pass


class OpenAIGPTGenerator(ChatGenerator):
    """Class for generating responses from the chatbot using OpenAI's GPT-3 API.
    """
    @staticmethod
    def generate_response(user_prompt):
        """Generates a response to the given prompt.
        :param user_prompt: str: The user prompt.
        :return: str: The response from the chatbot.
        """
        message_bot = generate_responses(user_prompt)
        return message_bot

    def respond(self, user_prompt):
        """Generates a response to the given prompt.
        :param user_prompt: str: The user prompt.
        :return: str: The response from the chatbot.
        """
        logging.info("Responding to user prompt: %s", user_prompt)
        response = self.generate_response(user_prompt)
        logging.info("Response to user prompt: %s", response)
        return response
