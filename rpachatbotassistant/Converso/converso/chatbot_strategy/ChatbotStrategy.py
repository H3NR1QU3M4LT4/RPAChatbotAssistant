from converso.AI.generator import ChatGenerator
from converso.AI.ner import NERStrategy
from converso.SendInformationRPAStrategy import SendInformationRPAStrategy


class ChatbotStrategy:
    def execute(self,
                input_text: str,
                response_generator: ChatGenerator,
                ner: NERStrategy = None,
                rpa_service: SendInformationRPAStrategy = None) -> str:
        pass
