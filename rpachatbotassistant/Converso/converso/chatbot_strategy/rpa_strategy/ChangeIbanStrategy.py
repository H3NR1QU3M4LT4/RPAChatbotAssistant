import re
from converso.chatbot_strategy.ChatbotStrategy import ChatbotStrategy
from converso.AI.generator import ChatGenerator
from converso.AI.ner import NERStrategy
from converso.SendInformationRPAStrategy import SendInformationRPAStrategy
from converso.chatbot_strategy.rpa_strategy.rpa.rpa_response import deliver_rpa_response
from converso.chatbot_strategy.rpa_strategy.rpa.contracts import User, NIBRequestObject


class ChangeIbanStrategy(ChatbotStrategy):
    def execute(self,
                input_text: str,
                response_generator: ChatGenerator,
                ner: NERStrategy = None,
                rpa_service: SendInformationRPAStrategy = None) -> str:

        entities = ner.extract_entities(input_text)["entities"]
        if entities.get("nib_iban"):
            entities["nib_iban"]["value"] = entities["nib_iban"]["value"].replace(" ", "").lower()
            pattern = re.compile(r"pt50\d{21}")
            if pattern.match(entities["nib_iban"]["value"]):
                object_request = NIBRequestObject(user=User(name="John Doe", phone_number="123456789"),
                                                  intention="change_nib_or_iban",
                                                  nib_iban=entities["nib_iban"]["value"])
                response_generator.respond(
                    "say something similar to this: 'The RPA service "
                    "will take care of this now.'")
                http_response = rpa_service.send_information(object_request)
                return deliver_rpa_response(http_response, response_generator, "NIB")
            else:
                return response_generator.respond(
                    "say something similar to this: 'The NIB you provided is not valid. "
                    "Please request again with a valid NIB.'")
        else:
            return response_generator.respond(
                "say something similar to this: 'I didn't understand the NIB you provided.'")
