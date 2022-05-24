from grammarChecker.util import *


def check_eitherneitherError(text):
    nlp = tagger(text)
    error_count = 0
    correct_text = ""
    word_count = 0                    # stores the count of the word stored in variable word
    count_nor = 0                     # stores the count of the occurance of word nor in a sentence
    word = ""                         # stores a word i.e. either or neither
    for sent in nlp:
        for index in range(len(sent)):
            # condition for checking if there is an either neither present in the sentence and is the present word is
            # a conjuction and adverb
            if index < len(sent)-1 and word_count == 1 and sent[index][1] in ['CC', 'RB']:
                if word == "either":
                    error_count += 1
                    correct_text += "or "
                    word_count = 0
                if word == "neither":
                    error_count += 1
                    correct_text += "nor "
                    word_count = 0
                continue
            # condition for checking if the word encountered is either
            if index < len(sent)-1 and sent[index][0] == "either" or sent[index][0] == "Either":
                word_count = 1
                word = "either"
                correct_text += sent[index][0]+" "
                continue
            # condition for checking if the word encountered is neither
            if index < len(sent)-1 and sent[index][0] == "neither" or sent[index][0] == "Neither":
                word_count = 1
                word = "neither"
                correct_text += sent[index][0]+" "
                continue
            else:
                correct_text += sent[index][0]+" "
                if sent[index][0] == "nor":  # condition for checking if the word encountered is nor
                    count_nor = 1
        first_word = correct_text.split()[0]
        # condition for checking if there is a nor present in the sentence without and neither or either as the first word.
        if count_nor == 1 and (first_word != "Neither" and first_word != "Either"):
            correct_text = "Neither "+correct_text
    return error_count, textFormatter(correct_text)
