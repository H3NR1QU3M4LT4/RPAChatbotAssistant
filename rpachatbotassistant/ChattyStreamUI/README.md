# ChattyStreamUI

ChattyStreamUI is a Python-based  project only responsible to show the UI to the final user, it calls the Converso Library that is responsible for every detail of the bot, generating responses and send the info to the RPA.

# Installation
To run this project first is required you to build the library Converso
* working directory: `ChattyStreamUI`
* `conda env create -f environment.yml`
* `poetry install`
* `cd ../Converso`
* `pip install dist/<file_name>.tar.gz`
* `cd ../ChattyStreamUI/chattystreamui`
* `streamlit run main.py`


# Project Organization

The project is organized into the following files and directories:

```
📦ChattyStreamUI
 ┣ 📂chattystreamui
 ┃ ┣ 📜.env
 ┃ ┣ 📜chatbot.py
 ┃ ┣ 📜main.py
 ┃ ┗ 📜test.py
 ┣ 📜Dockerfile
 ┣ 📜environment.yml
 ┣ 📜poetry.lock
 ┣ 📜pyproject.toml
 ┗ 📜README.md
```
