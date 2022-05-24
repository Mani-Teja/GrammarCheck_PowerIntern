# python -m unittest unitTest.py

import unittest
from nltk import pos_tag, word_tokenize
from grammarChecker.rules.article import check_articleError
from grammarChecker.rules.capitalization import check_capitalization
from grammarChecker.rules.pluralization import check_pluralization
from grammarChecker.rules.subVerb import check_SubVerbAgreement
from grammarChecker.rules.Because import check_becauseError
from grammarChecker.rules.apostrophe import check_apostropheError
from grammarChecker.rules.andError import and_check
from grammarChecker.rules.tense import check_TenseError
from grammarChecker.rules.But import check_butError
from grammarChecker.rules.eitherNeither import check_eitherneitherError
from grammarChecker.rules.althoughthough import check_althoughthoughError
from grammarChecker.rules.reflexError import check_reflexError


class TestGrammar(unittest.TestCase):
    def test_CapitalisationError(self):
        expected = "I was listening to the new Run the Jewels album. It is mostly hardcore Hip hop and I’ d heard " \
                   "about it through youtube Reviews online. Fantano scored it an 8."
        actual = check_capitalization([pos_tag(word_tokenize("I was listening to the new Run the jewels album. It is "
                                                             "mostly hardcore Hip hop and i’d heard about it through "
                                                             "youtube reviews online. Fantano scored it an 8"))])
        self.assertEqual(actual[1], expected)

    def test_AndError(self):
        expected = 'ajay and vijay are friends.'
        actual = and_check([pos_tag(word_tokenize("ajay vijay are friends"))])
        self.assertEqual(actual[1], expected)

    def test_SubVerbError(self):
        expected = "Sugar and flour is needed for the recipe."
        actual = check_SubVerbAgreement([pos_tag(word_tokenize("Sugar and flour are needed for the recipe."))])
        self.assertEqual(actual[1], expected)

    def test_ReflexError(self):
        expected = "andrew and I will conduct todays meet."
        actual = check_reflexError([pos_tag(word_tokenize("andrew and myself will conduct todays meet"))])
        self.assertEqual(actual[1], expected)

    def test_ArticleError(self):
        expected = "This morning I received an email from a friend who knows a lot about grammar and punctuation."
        actual = check_articleError([pos_tag(word_tokenize(
            "This morning I received a email from a friend who knows a lot about grammar and punctuation"))])
        self.assertEqual(actual[1], expected)

    def test_BecauseError(self):
        expected = (
            "The Prime Minister needs to come forward and address the nation because of this.Unless he assures "
            "everyone that the country is united against the fight with the invisible enemy, we will not be able to "
            "flourish.")
        actual = check_becauseError([pos_tag(word_tokenize(
            "The Prime Minister needs to come forward and address the nation because of this.Unless he assures "
            "everyone that the country is united against the fight with the invisible enemy,we will not be able to "
            "flourish because it."))])
        self.assertEqual(actual[1], expected)

    def test_TenseError(self):
        expected = "I have finished the report."
        actual = check_TenseError([pos_tag(word_tokenize("I have finish the report"))])
        self.assertEqual(actual[1], expected)

    def test_ButError(self):
        expected = "Anna is a highly intelligent girl, but she is rather lazy."
        actual = check_butError([pos_tag(word_tokenize("Anna is a highly intelligent girl,she is rather lazy"))])
        self.assertEqual(actual[1], expected)

    def test_eitherneitherError(self):
        expected = "Either we eat or we drink."
        actual = check_eitherneitherError([pos_tag(word_tokenize("Either we eat nor we drink"))])
        self.assertEqual(actual[1], expected)

    def test_althoughthoughError(self):
        expected = "Although he woke up late,he reached on time."
        actual = check_althoughthoughError([pos_tag(word_tokenize("Although he woke up late yet he reached on time"))])
        self.assertEqual(actual[1], expected)

    def test_apostropheError(self):
        expected = "they're leaving tomorrow for mum and dad's house."
        actual = check_apostropheError([pos_tag(word_tokenize("theyre leaving tomorrow for mum and dads house"))])
        self.assertEqual(actual[1], expected)

    def test_pluralizationError(self):
        expected = "there are many chocolates in the box."
        actual = check_pluralization([pos_tag(word_tokenize("there are many chocolate in the box"))])
        self.assertEqual(actual[1], expected)
