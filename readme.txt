                                            Grammar Correction using Rule Based System.

    This project is based on NLP(Natural Language Processing) which is a subfield of linguistics, computer science, and artificial intelligence concerned
with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language
data.

Objective: The aim is to design a model that successfully removes all grammatical errors from a sentence inputted by user. Different methods for error
corrections will be used in this project. The error correction methods used in this project are as follows:

1)Apostrophe Error:
    This method deals with the incorrect placement of the apostrophe symbol in a sentence. It also returns the error count and returns the correct text
which satisfies the use of apostrophe.

    Input parameters
        nlp : list of sentence tokenizers
    return parameters:
        error_count : integer
        correct_text : string

    Usage:
        from util.apostrophe import apostropheError
        import nltk
        text = input()
        print(apostropheError([nltk.pos_tag(text)]))

    eg 1:
        I/P: mum and dads house
        O/P: mum and dad's house
    eg 2:
        I/P: theyre leaving tomorrow
        O/P: they're leaving tomorrow

2)Article Error:
    This method deals with the wrong use of articles in a sentence. Additionally, it performs required modifications to make the text free from article
errors and returns the error count along with accurate text.

    Input parameters:
        nlp : list of sentence tokenizers

    return parameters:
        error_count : integer
        correct_text : string

    Usage:
        from util.article import check_articleError
        import nltk
        text = input()
        print(check_articleError([nltk.pos_tag(text)]))

  eg 1:

        I/P: I ate a apple.

        O/P: I ate an apple.

3)Capitalization Error:

  	This method deals with the case sensitivity of words. Additionally, it returns a sentence with correct case sensitivity and the error count.

Input parameters :

nlp : list of sentence tokenizers

Return parameters :

Error_count : integer

Correct_text : string

Usage:

from util.capitalization import check_capitalization

import nltk

text = input()

Print(check_capitalization([nltk.pos_tag(text)]))

  eg 1:

        I/P: shyam is my friend.

        O/P: Shyam is my friend.

4)Pluralization Error:

  This error deals with the wrong singular or plural usage of words in a sentence.

Input parameters :

nlp : list of sentence tokenizers

Return parameters :

Error_count : integer

Correct_text : string

Usage:

from util.pluralization import check_pluralization

import nltk

text = input()

Print(check_pluralization ([nltk.pos_tag(text)]))

  eg 1:

        I/P: there are many chocolate in the box.

        O/P: There are many chocolates in the box.



5)Spelling Error:

  This error checks the spelling errors in a sentence.

Input parameters :

data : string

Return parameters :

error_count : integer

mispelled : string

Usage:

from util.spell import spell_checker

import nltk

data = input()

Print(spell_checker (data)

  eg 1:

        I/P: amazing spiderman is out in theators.

        O/P: Amazing spiderman is out in theatres.



6)Subject Verb Agreement Error:

  This method checks and modifies the subject verb agreement related errors provided in a sentence. Additionally, it returns a sentence which follows subject verd agreement and the error count.

Input parameters :

nlp : list of sentence tokenizers

Return parameters :

Error_count : integer

Correct_text : string

Usage:

from util.subVerb import check_SubVerbAgreement

import nltk

text = input()

Print(check_SubVerbAgreement ([nltk.pos_tag(text)]))

Eg:

i/p: My dog wait for the postal carrier.

o/p: My dog waits for the postal carrier.

7)Because Error

  This error checks if text after using word 'because' incomplete sentence.

  Input parameters :

  nlp : list of sentence tokenizers

  Return parameters :

  Error_count : integer

  Correct_text : string

  Usage:

  from util.Because import check_becauseError

  import nltk

  text = input()

  Print(check_becauseError ([nltk.pos_tag(text)]))

  eg 1:

        I/O: There were so many people in the shop.

        O/P: There were so many people in the shop.

8)Tense Error

This error checks if the sentence has tense related errors.

Input parameters :

nlp : list of sentence tokenizers

Return parameters :

Error_count : integer

Correct_text : string

Usage:

from util.tense import check_TenseError

import nltk

text = input()

Print(check_TenseError ([nltk.pos_tag(text)]))

eg 1:

         I/O:She has know him for long time.

         O/P:She has known him for long time.



9) And Errror :

This method checks for the usage of ‘and’ conjunction used in the sentence provided. Aditionally it also modifies the incorrect usage and return the error count.

Input parameters:

nlp : list of sentense tokenizers

Return parameters:

Correct_text: String (modified sentence of the and conjunction)

Error_count : Integer (count of errors in the given text)

Usage :

Import nltk

from nltk import pos_tag,word_tokenize

from util.andError import and_check

Print(and_check([nltk.pos_tag(word_tokenize(input()))]))

Eg:

i/p: i like both coffee tea

o/p : i like both coffee and tea



10)But Error:

            This method checks for the usage of ‘but’ conjuction and ‘but ’ can also be used as preposition followed by noun.

Input parameters :

nlp : list of sentence tokenizers

Return parameters :

Error_count : integer

Correct_text : string

Usage:

from util.tense import check_ButError

import nltk

text = input()

Print(check_ButError ([nltk.pos_tag(text)]))



Eg 1:

      I/O: I refuse to discuss my medical history with anyone Dr Grant.

      O/P: I refuse to discuss my medical history with anyone but Dr Grant.

 11)Either Neither Error :

This method checks for the correct grammatical usage of Either/or and Neither/nor in sentences.

Input parameters :

nlp : list of sentence tokenizers

Return parameters :

Error_count : integer

Correct_text : string

Usage:

from util.eitherneither import eitherneitherError

import nltk

text = input()

Print(eitherneitherError ([nltk.pos_tag(text)]))



Eg 1:

      I/O: Either we dance else we sing.

      O/P: Either we dance or we sing.

12)Although Though Error:

This method checks for the correct grammatical usage Though/yet and Although/comma in sentences.

Input parameters :

nlp : list of sentence tokenizers

Return parameters :

Error_count : integer

Correct_text : string

Usage:

from util.althoughthough import althoughthoughError

import nltk

text = input()

Print(althoughthoughError ([nltk.pos_tag(text)]))



Eg 1:

      I/O: Though the attack happened ,the army survived

      O/P: Though the attack happened yet the army survived

13) Reflexive Pronoun Error :

This method checks for the irregular usage of reflex pronouns (himself, herself etc,). It eliminates , modifies the misused reflex pronouns and retruns the error count along with the correct sentence.

Input parameters:

  text : String

Return parameters:

  formatter : String

Usage:

from util.reflexError import check_reflexError

Text = input()

print(check_reflexError(text))

Example:

  I/P : andrew and myself will conduct todays meet.

  O/P : andrew and I will conduct todays meet.



14) Sentence Formatter:

  This module helps to format the given sentence into the readable format which doesn't have any indentation issues.

  Extra spaces at the Head and Tail of the sentences and irregular spaces in between the sentence are eliminated.

Input parameters:

  text : String

Return parameters:

  formatter : String

Usage:

from util.sentFormatter import textFormatter

Text = input()

print(textFormatter(text))

Example:

  I/P : I ‘m trying to make this task done on time .

  O/P : I’m trying to make this task done on time.

