import logging
import json
import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
import torch


def init():
    """
    This function is called when the container is initialized/started, typically after create/update of the deployment.
    You can write the logic here to perform init operations like caching the model in memory
    """
    global model
    global tokenizer
    global id2label

    # Load the fine-tuned Bert model and tokenizer using mlflow.pyfunc.load_model
    # Load the fine-tuned Bert model's config using AutoConfig
    model_config = AutoConfig.from_pretrained(
        os.path.join(os.getenv("AZUREML_MODEL_DIR"), "distilrobertav2-rpa-intentions/model/config.json")
    )

    # Read the JSON file and load it into a dictionary
    with open(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "distilrobertav2-rpa-intentions/model/config.json"), "r") \
            as json_file:
        id2label = json.load(json_file)["id2label"]

    # Load the fine-tuned Bert model using AutoModelForSequenceClassification
    model = AutoModelForSequenceClassification.from_pretrained(
        os.path.join(os.getenv("AZUREML_MODEL_DIR"), "distilrobertav2-rpa-intentions/model/pytorch_model.bin"),
        config=model_config,
    )
    tokenizer = AutoTokenizer.from_pretrained(
        os.path.join(os.getenv("AZUREML_MODEL_DIR"), "distilrobertav2-rpa-intentions/components/tokenizer")
    )
    logging.info("Init complete")


def run(raw_data):
    """
    This function is called for every invocation of the endpoint to perform the actual scoring/prediction.
    In the example we extract the data from the json input, tokenize the text, and call the fine-tuned Bert model's
    predict() method and return the result back
    """
    logging.info("model: request received")
    text = json.loads(raw_data)["text"]

    # Tokenize the text
    inputs = tokenizer(text, padding="max_length", truncation=True, max_length=128, return_tensors="pt")

    # Make prediction using the fine-tuned Bert model
    with torch.no_grad():
        outputs = model(**inputs)

    # Convert logits to probabilities using sigmoid activation
    sigmoid = torch.nn.Sigmoid()
    probabilities = sigmoid(outputs.logits).cpu().numpy().tolist()

    # Convert probabilities to list and return
    result = id2label[str(probabilities[0].index(max(probabilities[0])))]

    return result
