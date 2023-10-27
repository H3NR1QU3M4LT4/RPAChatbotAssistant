from converso.chatbot_strategy.ChatbotStrategy import ChatbotStrategy
from converso.AI.generator import ChatGenerator
from converso.AI.ner import NERStrategy
from converso.SendInformationRPAStrategy import SendInformationRPAStrategy
from converso.chatbot_strategy.rpa_strategy.merkle_data.table_room_offices import table_room_offices
from converso.chatbot_strategy.rpa_strategy.rpa.contracts import User, RoomTableOfficeRequestObject
from converso.chatbot_strategy.rpa_strategy.rpa.rpa_response import deliver_rpa_response


class RequestRoomTableOffice(ChatbotStrategy):

    def execute(self,
                input_text: str,
                response_generator: ChatGenerator,
                ner: NERStrategy = None,
                rpa_service: SendInformationRPAStrategy = None) -> str:

        entities = ner.extract_entities(input_text)["entities"]
        if (entities.get("table_room_office") and entities.get("date") and
                entities.get("office_location")):
            if entities["office_location"]["value"] in list(table_room_offices.keys()):
                if entities["table_room_office"]["value"] in table_room_offices[entities["office_location"]["value"]]:
                    object_request = RoomTableOfficeRequestObject(
                        user=User(name="John Doe", phone_number="123456789"),
                        intention="request_office_table_office",
                        date=entities["date"],
                        office_location=entities["office_location"],
                        table_room_office=entities["table_room_office"])

                    response_generator.respond(
                        "say something similar to this: 'The RPA service "
                        "will take care of this now.'")
                    http_response = rpa_service.send_information(object_request)
                    return deliver_rpa_response(http_response, response_generator, "room office, date and location")
            else:
                return response_generator.respond(
                    "say something similar to this: 'The information you provided is not valid. "
                    "Please request again with a valid location, date and parking lot.'")
        else:
            return response_generator.respond(
                "say something similar to this: 'I didn't understand the information you provided.'")
