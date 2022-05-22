from setuptools import setup, find_packages

setup(
    name="grammarChecker",
    version='0.1',
    description='Rule based grammar checker which works on NLP(Natural Language Processing) using NLTK library.',
    author='aviral mishra, chakori chaturvedi, maniteja penugonda',
    # packages=['grammarChecker', 'main', 'rules', 'spell_check', 'tests', 'util'],
    packages=find_packages(),
    install_requires=[
        'nltk',
        'pattern',
        'spellchecker'
    ]
)