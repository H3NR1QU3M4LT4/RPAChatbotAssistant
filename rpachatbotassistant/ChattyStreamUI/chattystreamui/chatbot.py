""" Chatbot module that contains the ChatBot class and its subclasses, as well as the BotFactory class to create the
chatbot instances and follow the Factory Design Pattern.
"""
import streamlit as st
from abc import ABC, abstractmethod
from converso.main import converso


class ChatBot(ABC):
    """
    Abstract class that defines the methods that a chatbot must implement.
    """
    @abstractmethod
    def generate_answer(self) -> None:
        """
        Generates an answer to the question posed by the user.
        :return: None
        """
        pass


class StandardBot(ChatBot):
    """
    Standard chatbot that uses the converso library to generate an answer to the question posed by the user.
    """
    def __init__(self):
        pass

    def generate_answer(self) -> None:
        """
        Generates an answer to the question posed by the user.
        :return: None
        """
        user_message = st.session_state.input_text
        message_title = "Standard Bot\n\n"
        message_bot = converso(user_message)
        st.session_state.history.append({"message": user_message, "is_user": True})
        st.session_state.history.append({"message": message_title + message_bot, "is_user": False})
        st.session_state.input_text = ""


class CustomBot(ChatBot):
    """
    Custom chatbot that generates a custom answer to the question posed by the user.
    """
    def __init__(self):
        pass

    def generate_answer(self) -> None:
        """
        Generates an answer to the question posed by the user.
        :return: None
        """
        user_message = st.session_state.input_text
        message_title = "Advanced Bot\n\n"
        message_bot = "Advanced Bot Message"
        st.session_state.history.append({"message": user_message, "is_user": True})
        st.session_state.history.append({"message": message_title + message_bot, "is_user": False})
        st.session_state.input_text = ""


class BotFactory:
    """
    Factory class that creates the chatbot instances.
    """
    @staticmethod
    def create_bot(bot_type: str) -> ChatBot:
        """
        Creates the chatbot instance.
        :param bot_type: str -> type of chatbot to create
        :return: ChatBot instance -> chatbot instance
        """
        if bot_type == "standard":
            return StandardBot()
        elif bot_type == "custom":
            return CustomBot()
        else:
            raise ValueError("Invalid bot type")
