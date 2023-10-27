from .ChatbotStrategy import ChatbotStrategy
from converso.AI.generator import ChatGenerator
from converso.AI.ner import NERStrategy
from converso.SendInformationRPAStrategy import SendInformationRPAStrategy


def chatbot_conversational_strategy_handler(intention, prompt,
                                            response_generator):
    if intention['intention'] == 'greetings':
        return GreetingsStrategy().execute(prompt, response_generator)
    elif intention['intention'] == 'goodbye':
        return GoodbyeStrategy().execute(prompt, response_generator)
    else:
        return NothingRelatedStrategy().execute(prompt, response_generator)


class GreetingsStrategy(ChatbotStrategy):
    def execute(self,
                input_text: str,
                response_generator: ChatGenerator,
                ner: NERStrategy = None,
                rpa_service: SendInformationRPAStrategy = None) -> str:
        response = response_generator.respond(input_text)
        return response


class GoodbyeStrategy(ChatbotStrategy):
    def execute(self,
                input_text: str,
                response_generator: ChatGenerator,
                ner: NERStrategy = None,
                rpa_service: SendInformationRPAStrategy = None) -> str:
        response = response_generator.respond(input_text)
        return response


class NothingRelatedStrategy(ChatbotStrategy):
    def execute(self,
                input_text: str,
                response_generator: ChatGenerator,
                ner: NERStrategy = None,
                rpa_service: SendInformationRPAStrategy = None) -> str:
        response = response_generator.respond(
            "say something similar to this: 'I understand and I could help you with that! "
            "However your request is not related to my actual responsibilities.'"
        )
        return response
