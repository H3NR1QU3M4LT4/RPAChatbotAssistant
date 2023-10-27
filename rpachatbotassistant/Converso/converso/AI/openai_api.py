"""This module is used to generate responses from the OpenAI API.
"""
import os
import logging
from dotenv import load_dotenv
import openai
import time

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_type = os.getenv('OPENAI_API_TYPE')
openai.api_base = os.getenv('OPENAI_API_BASE')
openai.api_version = os.getenv('OPENAI_API_API_VERSION')


def generate_responses(prompt: str) -> str:
    """ Generates responses from the OpenAI API.
    :param prompt: str: The prompt to be sent to the user.
    :return: str: The response from the OpenAIGPTGenerator.
    """
    logging.info("Generating responses for user prompt")
    time.sleep(11)
    message_bot = openai.ChatCompletion.create(engine="testgpt35turbo",
                                               messages=[{"role": "user", "content": prompt}],
                                               temperature=0.7,
                                               max_tokens=100,
                                               top_p=0.95,
                                               frequency_penalty=0,
                                               presence_penalty=0,
                                               stop=None)
    message_bot = message_bot["choices"][0]["message"]["content"]
    logging.info("Generated responses")
    return message_bot
