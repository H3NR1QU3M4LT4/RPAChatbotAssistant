# DistilDataQuarry

This folder name emphasizes the use of DistilBert as a tool for distilling information from raw data and evokes the idea of mining valuable insights from raw data, emphasizing the importance of preprocessing in the machine learning workflow.
The DistilDataQuarry is where I store all of the data preprocessing and model training work for this machine learning project.
I used DistilBert model to recognize intentions and for NER. For the training for this machine  learning model I used PyTorch. 

This is only to build DistilBERT models for NER and text classification.


# Project Organization
```
📦DistilDataQuarry
 ┣ 📂data
 ┃ ┣ 📂external
 ┃ ┃ ┗ 📜.gitkeep
 ┃ ┣ 📂interim
 ┃ ┃ ┗ 📜.gitkeep
 ┃ ┣ 📂processed
 ┃ ┃ ┗ 📜.gitkeep
 ┃ ┗ 📂raw
 ┃ ┃ ┣ 📜.gitkeep
 ┃ ┃ ┣ 📜NIB.txt
 ┃ ┃ ┣ 📜parking_lot.py
 ┃ ┃ ┣ 📜parking_lot.txt
 ┃ ┃ ┣ 📜rooms.py
 ┃ ┃ ┣ 📜rooms.txt
 ┃ ┃ ┣ 📜test_intents.py
 ┃ ┃ ┗ 📜time_off.txt
 ┣ 📂docs
 ┃ ┣ 📂wiki
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📜conf.py
 ┃ ┣ 📜getting-started.rst
 ┃ ┣ 📜index.rst
 ┃ ┣ 📜make.bat
 ┃ ┗ 📜Makefile
 ┣ 📂models
 ┃ ┣ 📂version-1
 ┃ ┃ ┣ 📜.DS_Store
 ┃ ┃ ┗ 📜distilbert-model-1
 ┃ ┗ 📜.gitkeep
 ┣ 📂notebooks
 ┃ ┣ 📜.gitkeep
 ┃ ┣ 📜NIB-intent.ipynb
 ┃ ┗ 📜NIB-ner.ipynb
 ┣ 📂references
 ┃ ┗ 📜.gitkeep
 ┣ 📂src
 ┃ ┣ 📂data
 ┃ ┃ ┣ 📜.gitkeep
 ┃ ┃ ┣ 📜make_dataset.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂features
 ┃ ┃ ┣ 📜.gitkeep
 ┃ ┃ ┣ 📜build_features.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂models
 ┃ ┃ ┣ 📜.gitkeep
 ┃ ┃ ┣ 📜predict_model.py
 ┃ ┃ ┣ 📜train_model.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂visualization
 ┃ ┃ ┣ 📜.gitkeep
 ┃ ┃ ┣ 📜visualize.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.env
 ┣ 📜Makefile
 ┣ 📜README.md
 ┣ 📜setup.py
 ┣ 📜test_environment.py
 ┗ 📜tox.ini
```

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
