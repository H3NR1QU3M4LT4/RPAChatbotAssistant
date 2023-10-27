from converso.chatbot_strategy.ChatbotStrategy import ChatbotStrategy
from converso.AI.generator import ChatGenerator
from converso.AI.ner import NERStrategy
from converso.SendInformationRPAStrategy import SendInformationRPAStrategy
from converso.chatbot_strategy.rpa_strategy.rpa.contracts import User, TimeOffRequestObject
from converso.chatbot_strategy.rpa_strategy.rpa.rpa_response import deliver_rpa_response


class RequestTimeOffStrategy(ChatbotStrategy):

    def execute(self,
                input_text: str,
                response_generator: ChatGenerator,
                ner: NERStrategy = None,
                rpa_service: SendInformationRPAStrategy = None) -> str:
        # Check if the input contains the keyword "request time off"
        # If yes, extract the date range from the input
        # If the date range is valid, return a success message
        # If not, return a message asking the user to provide a valid date range
        entities = ner.extract_entities(input_text)["entities"]

        if entities.get("date"):
            object_request = TimeOffRequestObject(user=User(name="John Doe", phone_number="123456789"),
                                                  intention="request_time_off",
                                                  date=entities["date"]["value"])

            return generate_strategy(response_generator, rpa_service, object_request)

        elif entities.get("date_range"):
            object_request = TimeOffRequestObject(user=User(name="John Doe", phone_number="123456789"),
                                                  intention="request_time_off",
                                                  date=entities["date_range"]["value"])

            return generate_strategy(response_generator, rpa_service, object_request)

        else:
            return response_generator.respond(
                "say something similar to this: 'The information you provided is not valid. "
                "Please request again with a valid date.'")


def generate_strategy(response_generator, rpa_service, object_request):
    response_generator.respond(
        "say something similar to this: 'The RPA service "
        "will take care of this now.'")
    http_response = rpa_service.send_information(object_request)
    return deliver_rpa_response(http_response, response_generator, "date")
