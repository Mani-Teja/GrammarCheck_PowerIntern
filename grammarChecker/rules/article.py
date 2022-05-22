"""Function build by Chakori Chaturvedi for checking article errors in a given sentence.
   eg 1:-
         I/P:I ate a apple.
         O/P:I ate an apple.
"""
from nltk.tokenize import word_tokenize
from pattern.en import referenced
from grammarChecker.util import *


def check_articleError(nlp):
    error_count = 0
    correct_text = ""
    for sent in nlp:
        for index in range(len(sent)):
            if sent[index][0] in ['a', 'an']:
                # to check whether the (i)th word is in text file or tag of (i+1)th word is plural noun(eg cats,
                # pencils) or proper noun,plural(eg Indians,Americans)
                if sent[index + 1][1] in ["NNS", "NNPS"]:
                    error_count += 1
                # to check whether the tag of(i+1)th word is adjective(large, fast, honest) and the tag of (i+2)th
                # word is plural noun
                elif index < len(sent)-2 and sent[index+1][1] in ["JJ", "JJR"] and sent[index+2][1] in ['NNP', 'NN']:
                    """
                    referenced provides appropriate article before the word 
                    eg:
                        I/P: referenced(hour)
                        O/P: an hour
                    """    
                    # to check whether (i)th word equals 'a'  and reference of next word equals 'an '+(i+1)th word
                    if sent[index][0] == 'a' and referenced(sent[index + 1][0]) == ('an ' + sent[index + 1][0]):
                        correct_text += 'an'
                        error_count += 1
                    # to check whether (i)th word equals 'an'  and reference of next word equals 'a '+(i+1)th word
                    elif sent[index][0] == 'an' and referenced(sent[index + 1][0]) == ('a ' + sent[index + 1][0]):
                        correct_text += 'a'
                        error_count += 1
                    else:
                        correct_text += sent[index][0]
                elif sent[index + 1][1] not in ["NNP", "NN"]:
                    error_count += 1
                # to check whether (i)th word equals 'a'  and reference of next word equals 'an '+(i+1)th word
                elif sent[index][0] == 'a' and referenced(sent[index + 1][0]) == ('an ' + sent[index + 1][0]):
                    correct_text += 'an'
                    error_count += 1
                # to check whether (i)th word equals 'an'  and reference of next word equals 'a '+(i+1)th word
                elif sent[index][0] == 'an' and referenced(sent[index + 1][0]) == ('a ' + sent[index + 1][0]):
                    correct_text += 'a'
                    error_count += 1
                else:
                    correct_text += sent[index][0]
                correct_text += " "
            else:
                correct_text += sent[index][0]
                correct_text += " "
    return error_count, textFormatter(correct_text)
