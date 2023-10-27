""" Main entry point for the chatbot. It uses a streamlit app to display the chatbot interface.
The algorithm is based on fine-tuning the Distil-Bert model to predict the intent of the user
and NER to extract the entities.
"""
import os
from dotenv import load_dotenv
import openai
import streamlit as st
from streamlit_chat import message as st_message
import uuid

from chatbot import BotFactory


load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_type = os.getenv('OPENAI_API_TYPE')
openai.api_base = os.getenv('OPENAI_API_BASE')
openai.api_version = os.getenv('OPENAI_API_API_VERSION')


def main() -> None:
    """
    Main entry point for the chatbot.
    :return: None
    """
    if "history" not in st.session_state:
        st.session_state.history = []

    st.set_page_config(page_title="RPAChatbotAssistant",
                       page_icon=":robot_face:",
                       layout="wide")
    st.markdown("<h2 style='text-align: center;'>RPAChatbotAssistant 😬</h2>",
                unsafe_allow_html=True)
    st.write(
        "Welcome to the chatbot. Please type a message and press Enter to start the conversation."
    )

    bot_factory = BotFactory()
    bot = bot_factory.create_bot("standard")

    for chat in st.session_state.history:
        if chat["is_user"]:
            st_message(chat["message"], avatar_style="personas", is_user=True, key=str(uuid.uuid4()))
        else:
            st_message(chat["message"],
                       avatar_style="bottts",
                       seed="Smokey",
                       is_user=False,
                       key=str(uuid.uuid4()))

    st.text_input("Talk to the bot",
                  key="input_text",
                  on_change=bot.generate_answer)


if __name__ == "__main__":
    main()
