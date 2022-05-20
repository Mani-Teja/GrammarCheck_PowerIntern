"""Function built by Aviral Mishra for checking Apostrophe Error.
   eg 1:
        I/P:mum and dads house
        O/P:mum and dad's house
   eg 2:
        I/P:theyre leaving tomorrow
        O/P:they're leaving tomorrow
"""
from nltk import word_tokenize, pos_tag
from grammarChecker.util import textFormatter


def check_apostropheError(nlp):
    error_count = 0
    flag = False      # boolean flag to check if the final if condition is executed successfully
    correct_text = ""
    suffixList = ["m", "re", "t", "s", "ll", "ve", "d"]
    for sent in nlp:
        for index in range(len(sent)):
            if index < len(sent)-1 and sent[index][1] in ['WRB', 'MD', 'PRP', 'PRP$', 'VBZ', 'RB', 'NNP', 'VBP', 'NN', 'VBD', 'NNS', 'VB', 'JJ'] \
                    and sent[index+1][1] in ['VBP', 'VBG', 'VBD', 'JJ', 'VB', 'NN', 'IN']:
                if sent[index][1] == "VBZ" and sent[index + 1][1] == "JJ":             # special case of is(i's)
                    correct_text += sent[index][0]+" "
                else:
                    for suffix in suffixList:                                # loop traversing through suffixList
                        if sent[index][0].endswith(suffix):  # checking if the token ends with a particular suffix
                            if suffix == 't' and sent[index][0].endswith("nt"):             # special case of nt
                                length = len(suffix)
                                prp_word = sent[index][0][slice(-length)]               # slicing the suffix
                                prp_word = pos_tag(word_tokenize(prp_word))
                                if prp_word[0][1] in ['VBP', 'VB', 'MD']:
                                    correct_text += prp_word[0][0]+"n'"+suffix+" "      # don't,can't,shouldn't
                                    error_count += 1
                                    flag = True
                                    break
                            length = len(suffix)                                        # length of the particular token
                            prp_word = sent[index][0][slice(-length)]                     # slicing the suffix
                            prp_word = pos_tag(word_tokenize(prp_word))
                            if prp_word[0][1] in ['PRP', 'NN']:
                                correct_text += prp_word[0][0]+"'"+suffix+" "
                                error_count += 1
                                flag = True
                                break
                    if not flag:
                        correct_text += sent[index][0]+" "
            else:
                correct_text += sent[index][0]+" "
            flag = False
    return error_count, textFormatter(correct_text)
