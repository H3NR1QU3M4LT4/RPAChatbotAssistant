from setuptools import setup, find_packages

setup(
    name="converso",
    version="0.1.0",
    author="Henrique Malta",
    author_email="silvinohenrique.teixeiramalta@isobar.onmicrosoft.com",
    description="A Python Library to generate responses from user prompt",
    license="MIT",
    packages=find_packages(include=('converso*',)),
    install_requires=[
        "openai", " python-dotenv"
    ],
)
