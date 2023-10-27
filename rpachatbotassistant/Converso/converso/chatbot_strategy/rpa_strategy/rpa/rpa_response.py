from converso.chatbot_strategy.rpa_strategy.rpa.contracts import User


user = User(name="John Doe", phone_number="123456789")


def deliver_rpa_response(http_response, response_generator, entity):
    if http_response.get("status_code"):
        if http_response.get("status_code") == 200:
            return response_generator.respond(
                "say something similar to this: 'Your request has been successfully processed by the RPA service.'")
        else:
            return response_generator.respond(
                f"say something similar to this: 'Unfortunately, the RPA service was unable to process your {entity} "
                "at this time. Please try again later.'")
    else:
        return response_generator.respond(
            "say something similar to this: 'I apologize for the inconvenience, but I am unable to establish contact "
            "with the RPA service at this time. Please try again later.'")
