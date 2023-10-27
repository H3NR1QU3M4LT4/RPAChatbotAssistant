from converso.chatbot_strategy.ChatbotStrategy import ChatbotStrategy
from converso.AI.generator import ChatGenerator
from converso.AI.ner import NERStrategy
from converso.SendInformationRPAStrategy import SendInformationRPAStrategy
from converso.chatbot_strategy.rpa_strategy.merkle_data.parking_lots import parking_lots
from converso.chatbot_strategy.rpa_strategy.rpa.contracts import User, ParkingLotRequestObject
from converso.chatbot_strategy.rpa_strategy.rpa.rpa_response import deliver_rpa_response


class RequestParkingLotStrategy(ChatbotStrategy):

    def execute(self,
                input_text: str,
                response_generator: ChatGenerator,
                ner: NERStrategy = None,
                rpa_service: SendInformationRPAStrategy = None) -> str:
        # Check if the input contains the keyword "request parking lot"
        # If yes, extract the parking lot location from the input
        # If the location is valid, return a success message
        # If not, return a message asking the user to provide a valid location
        entities = ner.extract_entities(input_text)["entities"]
        if (entities.get("parking_lot") and entities.get("date") and
                entities.get("office_location")):
            if entities["office_location"]["value"] in list(parking_lots.keys()):
                if entities["parking_lot"]["value"] in parking_lots[entities["office_location"]["value"]]:
                    object_request = ParkingLotRequestObject(user=User(name="John Doe", phone_number="123456789"),
                                                             intention="request_parking_lot",
                                                             date=entities["date"]["value"],
                                                             office_location=entities["office_location"]["value"],
                                                             parking_lot=entities["parking_lot"]["value"])

                    response_generator.respond(
                        "say something similar to this: 'The RPA service "
                        "will take care of this now.'")
                    http_response = rpa_service.send_information(object_request)
                    return deliver_rpa_response(http_response, response_generator, "parking lot, date and location")
            else:
                return response_generator.respond(
                        "say something similar to this: 'The information you provided is not valid. "
                        "Please request again with a valid location, date and parking lot.'")

        else:
            return response_generator.respond(
                "say something similar to this: 'I didn't understand the information you provided.'")
