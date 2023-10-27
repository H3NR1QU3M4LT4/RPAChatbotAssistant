"""This module is responsible for sending the information to the RPA Service.
"""
from dataclasses import asdict
import json
import logging
import requests


class SendInformationRPAStrategy:
    """Abstract class for sending the information to the RPA Service."""

    def send_information(self, object_request):
        """Sends the information to the RPA Service.
        :param object_request: str: The object request based on the intention.
        :return: str: The response from the RPA Service."""
        pass


class HttpSendInformationRPAStrategy(SendInformationRPAStrategy):
    """Class for sending the information to the RPA Service using HTTP."""

    def send_information(self, object_request):
        """Sends the information to the RPA Service.
        :param object_request: str: The user's message.
        :return: str: The response from the RPA Service.
        """
        try:
            object_request = asdict(object_request)
            rpa_response = requests.post("http://127.0.0.1:5000/rpa",
                                         json=json.dumps(object_request))
            logging.info(f"Content: {rpa_response.content} Status Code: {rpa_response.status_code}")
            rpa_response = {
                "status_code": rpa_response.status_code,
                "message": rpa_response.content
            }
        except Exception as e:
            logging.error(e)
            rpa_response = {
                "exception":
                f"{e}",
                "message":
                "It was not possible to send the information to the RPA Service."
            }

        return rpa_response
