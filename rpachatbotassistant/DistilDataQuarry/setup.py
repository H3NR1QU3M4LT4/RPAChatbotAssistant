from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description=
    """The DistilDataQuarry is where I store all of the data preprocessing and model training work 
                    for this machine learning project.
                    I used DistilBert model to recognize intentions and for NER. For the training for this machine 
                    learning model I used PyTorch. """,
    author='Silvino Henrique Teixeira Malta',
    license='MIT',
)
