#python -m unittest test.py

import unittest
from nltk import pos_tag , word_tokenize
from nltk import pos_tag,word_tokenize
from util.spell import spell_checker
from util.article import check_articleError
from util.capitalization import check_capitalization
from util.pluralization import check_pluralization
from util.subVerb import check_SubVerbAgreement
from util.Because import check_becauseError
from util.apostrophe import apostropheError
from util.andError import and_check
from util.tense import check_TenseError
from util.But import check_butError
from util.eitherNeither import check_eitherneitherError
from util.althoughthough import check_althoughthoughError
from util.reflexError import check_reflexError

class TestGrammar(unittest.TestCase) :
    def test_CapitalisationError(self) :
        expected = 'I was listening to the new Run the Jewels album . It is mostly hardcore Hip hop and I ’ d heard about it through youtube Reviews online . Fantano scored it an 8 '
        actual =check_capitalization([pos_tag(word_tokenize("I was listening to the new Run the jewels album. It is mostly hardcore Hip hop and i’d heard about it through youtube reviews online. Fantano scored it an 8"))])
        self.assertEqual(actual[1] , expected)

    def test_ArticleError(self) :
        expected = "I ate an apple "
        actual = check_articleError([pos_tag(word_tokenize("I ate a apple"))])
        self.assertEquals(actual[1] , expected)

    def test_AndError(self) :
        expected = 'ajay and vijay are friends'
        actual =and_check([pos_tag(word_tokenize("ajay vijay are friends"))])
        self.assertEqual(actual[1] , expected)

    def test_SubVerbError(self) :
        expected = 'Sugar and flour are needed for the recipe. '
        actual = check_SubVerbAgreement([pos_tag(word_tokenize("Sugar and flour is needed for the recipe."))])
        self.assertEqual(actual[1] , expected)

    def test_ReflexError(self) :
        expected = 'andrew and I will conduct todays meet '
        actual =check_reflexError([pos_tag(word_tokenize("andrew and myself will conduct todays meet"))])
        self.assertEqual(actual[1] , expected)
        
    def test_ArticleError(self) :
        expected = ("This morning I received an email from a friend who knows a lot about grammar and punctuation ")
        actual =check_articleError([pos_tag(word_tokenize("This morning I received a email from a friend who knows a lot about grammar and punctuation"))])
        self.assertEqual(actual[1] , expected)

    def test_BecauseError(self) :
        expected = ("The Prime Minister needs to come forward and address the nation because of this.Unless he assures everyone that the country is united against the fight with the invisible enemy , we will not be able to flourish .")
        actual =check_becauseError([pos_tag(word_tokenize("The Prime Minister needs to come forward and address the nation because of this.Unless he assures everyone that the country is united against the fight with the invisible enemy,we will not be able to flourish because it."))])
        self.assertEqual(actual[1] , expected)
        

    def test_TenseError(self) :
        expected = ("I have finished the report ")
        actual =check_TenseError([pos_tag(word_tokenize("I have finish the report"))])
        self.assertEqual(actual[1] , expected)    
