"""Function built by Aviral Mishra for checking Pluralization Error
   eg 1:
        I/P:there are many chocolate in the box.
        O/P:There are many chocolates in the box.
"""

from pattern.text.en import pluralize, singularize
from grammarChecker.util import *


def check_pluralization(text):
    nlp = tagger(text)
    error_count = 0
    correct_text = ""
    for sent in nlp:
        for index in range(len(sent)):
            # if condition for checking if the token encountered has cardinal digit as a previous token.
            if index != len(sent)-1 and sent[index][1] in ['NN', 'NNP', 'NNS', 'NNPS'] and (sent[index-1][1] in ['CD'] or sent[index+1][1] == 'POS'):
                correct_text += sent[index][0]
                continue
            # if condition for checking if the token encountered is singular noun or a singular pronoun.
            if index != len(sent)-1 and sent[index][1] in ['NN', 'NNP', 'NNS']:
                # if condition for checking if the singular noun or pronoun encountered is being followed by a (verb
                # or singular verb in present tense) or has a (verb or singular verb in present tense or adjective)
                # as its previous token.
                if sent[index+1][1] == 'VB' or sent[index-1][1] in ['VB', 'VBP'] or sent[index-1][0] == "many" \
                        or sent[index-2][0] in ["lot", "excess"]:
                    error_count += 1
                    correct_text += pluralize(sent[index][0])+" "
                else:
                    correct_text += sent[index][0]+" "
            # if condition for checking if the token encountered is plural noun or a plural pronoun.
            elif index != len(sent)-1 and sent[index][1] in ['NNS', 'NNPS']:
                # if condition for checking if the plural noun or pronoun encountered is being followed by a (plural
                # noun or singular verb in present tense in 3rd person) or has a (determiner) as its previous token.
                if sent[index+1][1] in ['VBZ', 'NNS'] or sent[index-1][1] in ['DT']:
                    correct_text += singularize(sent[index][0])+" "
                else:
                    correct_text += sent[index][0]+" "
            # if condition for checking if the token encountered is a cardinal digit.
            elif index != len(sent)-1 and sent[index][1] in ['CD']:
                # if condition for checking if the cardinal digit encountered is one(1).
                if sent[index][0] in ["1", "one"]:
                    # if condition for checking if the cardinal digit encountered is being followed by a plural noun or plural pronoun.
                    if sent[index+1][1] in ['NNS', 'NNPS']:
                        error_count += 1
                        correct_text += sent[index][0]+" "+singularize(sent[index+1][0])+" "
                else:
                    # if condition for checking if the cardinal digit encountered is being followed by a singular noun or singular pronoun.
                    if sent[index+1][1] in ['NNP', 'NNS']:
                        error_count += 1
                        correct_text += sent[index][0]+" "+pluralize(sent[index+1][0])+" "
            else:
                correct_text += sent[index][0]+" "
    return error_count, textFormatter(correct_text)
