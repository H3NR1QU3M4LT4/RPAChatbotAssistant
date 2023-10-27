# Converso

Converso is a Python-based library project that combines the power of OpenAI's GPT-3 API or a fine-tuned pre-trained model DistilBERT for intent and entity recognition and a generator. This library is responsible to generate responses and get the meaning behind the user prompt and send the information to a RPA service to automate the service.
This library receives the user prompt, find the user intention, recognize the main entities and send them to a RPA service. Also implements the whole chatbot logic.

# Installation
This project is not meant to be executed, it works like a library
* `conda env create -f environment.yml`
* `poetry install`
* `poetry build`
# Project Organization

The project is organized into the following files and directories:

* converso: This directory contains the main modules and classes for the chatbot project.
    * AI: This subdirectory contains modules for different AI services used in the project, including OpenAI's GPT-3 API, DistilBERT for intent and entity recognition, and others.
    * converso_factory.py: This module contains a factory class that creates instances of the different AI services used in the project.
    * main.py: This module contains the main function for running the chatbot.
    * send_information_rpa.py: This module contains a service for sending information to a Robotic Process Automation (RPA) system.
* .env: This file contains environment variables required for running the project, including the OpenAI API key, type, base, and version.
* environment.yml: This file contains the dependencies required for the project.
* poetry.lock: This file contains the locked dependencies for the project.
* pyproject.toml: This file contains the project metadata and configuration for Poetry.
* README.md: This file contains information about the project.
* setup.py: This file contains the setup script for the project.

```
📦Converso
 ┣ 📂converso
 ┃ ┣ 📂AI
 ┃ ┃ ┣ 📜generator.py
 ┃ ┃ ┣ 📜intentions_entities.py
 ┃ ┃ ┣ 📜intent_recognition.py
 ┃ ┃ ┣ 📜ner.py
 ┃ ┃ ┣ 📜openai_api.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┗ 📜__init__.cpython-39.pyc
 ┃ ┣ 📜converso_factory.py
 ┃ ┣ 📜main.py
 ┃ ┣ 📜send_information_rpa.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.env
 ┣ 📜environment.yml
 ┣ 📜poetry.lock
 ┣ 📜pyproject.toml
 ┣ 📜README.md
 ┣ 📜setup.py
 ┗ 📜test.py
```

# Conclusion
Converso is a powerful library project that combines the power of OpenAI's GPT-3 API or with a fine-tuned pre-trained model DistilBERT for intent and entity recognition. With its versatile conversation capabilities, Converso is an excellent tool for automating customer service, technical support, and other chat-based interactions.