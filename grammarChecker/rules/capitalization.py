"""Function built by Sai Maniteja Penugonda for checking Capitalization Error
   eg 1:
        I/P:shyam is my friend.
        O/P:Shyam is my friend.
"""
from grammarChecker.util import *


def days(word):
    if word in ['january', 'feburary', 'march', 'april', 'may', 'june', 'july', 'august', 'june', 'july', 'august',
                'september', 'october', 'november', 'december']:
        return True
    if word in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        return True
    pass


def check_capitalization(text):
    nlp = tagger(text)
    error_count = 0
    correct_text = ''
    punc = False
    for sent in nlp:
        for index in range(len(sent)):
            # if condition for checking if tag encountered is proposition or noun plural
            if index == 0 or sent[index][1] in ['JJ', 'NNP', 'NNPS'] or punc or days(sent[index][0].lower()):
                if punc:
                    punc = False
                # if condition for checking if token encountered is in lowercase
                if sent[index][0].islower():
                    error_count += 1
                    correct_text += sent[index][0].capitalize() + ' '
                else:
                    correct_text += sent[index][0] + ' '
            # if condition for checking if the token encountered is'i'
            elif sent[index][0] == 'i':
                error_count += 1
                correct_text += 'I '
            else:
                if sent[index][0] in '.,()[]{}\'\"':
                    punc = True
                correct_text += sent[index][0].lower()+' '
    return error_count, textFormatter(correct_text)
