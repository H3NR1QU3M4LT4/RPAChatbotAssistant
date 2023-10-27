""" Flask application for the RPA simulator that receives information from the chatbot and sends it to the RPA.
"""
from flask import Flask, request
import json
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello_world():
    """
    Default endpoint for the application
    """
    return 'Hello World!'


@app.route('/rpa',  methods=['GET', 'POST'])
def receive_information_chatbot():
    """
    Endpoint for receiving information from the chatbot and sending it to the RPA
    ---
    parameters:
      - name: message
        in: body
        required: true
        type: string
        description: JSON message containing information from the chatbot
    responses:
        200:
            description: JSON message containing information sent to the RPA
    """
    if request.method == 'GET':
        return "This is a GET request."
    elif request.method == 'POST':
        data = request.get_json()
        logging.info(json.loads(data))
        return data


if __name__ == '__main__':
    app.run()
