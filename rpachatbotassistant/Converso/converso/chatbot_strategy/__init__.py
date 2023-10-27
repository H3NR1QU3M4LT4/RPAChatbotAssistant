from converso.chatbot_strategy.conversational_strategy_handler import chatbot_conversational_strategy_handler
from converso.chatbot_strategy.rpa_strategy_handler import chatbot_rpa_strategy_handler


def chatbot_strategy_handler(intention, prompt, response_generator, ner, rpa_service):
    if (intention['intention'] == 'greetings') \
            or (intention['intention'] == 'goodbye_prompt') \
            or (intention['intention'] == 'nothing_related'):
        return chatbot_conversational_strategy_handler(intention, prompt, response_generator)
    else:
        return chatbot_rpa_strategy_handler(intention, prompt, response_generator, ner, rpa_service)
