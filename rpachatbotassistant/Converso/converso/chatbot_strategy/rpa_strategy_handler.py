""" This module is responsible for handling the RPA strategy.
"""
from converso.chatbot_strategy.conversational_strategy_handler import NothingRelatedStrategy
from converso.chatbot_strategy.rpa_strategy.ChangeIbanStrategy import ChangeIbanStrategy
from converso.chatbot_strategy.rpa_strategy.RequestParkingLotStrategy import RequestParkingLotStrategy
from converso.chatbot_strategy.rpa_strategy.RequestRoomTableOffice import RequestRoomTableOffice
from converso.chatbot_strategy.rpa_strategy.RequestTimeOffStrategy import RequestTimeOffStrategy


def chatbot_rpa_strategy_handler(intention, prompt, response_generator, ner,
                                 rpa_service):
    if intention['intention'] == 'change_nib_or_iban':
        return ChangeIbanStrategy().execute(prompt, response_generator, ner,
                                            rpa_service)
    elif intention['intention'] == 'request_time_off':
        return RequestTimeOffStrategy().execute(prompt, response_generator, ner,
                                                rpa_service)
    elif intention['intention'] == 'request_office_table_office':
        return RequestRoomTableOffice().execute(prompt, response_generator, ner,
                                                rpa_service)
    elif intention['intention'] == 'request_parking_lot':
        return RequestParkingLotStrategy().execute(prompt, response_generator, ner,
                                                   rpa_service)
    else:
        return NothingRelatedStrategy().execute(prompt, response_generator)
