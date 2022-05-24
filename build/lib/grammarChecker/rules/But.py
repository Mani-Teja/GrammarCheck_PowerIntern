from grammarChecker.util import *


def check_butError(text):
    nlp = tagger(text)
    error_count = 0
    correct_text = ''
    for sent in nlp:
        for index in range(len(sent)-1):
            correct_text += sent[index][0] + ' '
            # if the token encountered is ','
            if sent[index][1] in [',']:
                if sent[index-1][1] in ['NN', 'NNP', 'NNS', 'NNPS'] and sent[index+1][1] in ['NN', 'NNS', 'NNP', 'NNPS']:
                    correct_text += ' '
                else:
                    correct_text += 'but '
                    error_count += 1
            # if the token encountered is noun and the next token encountered is also noun, determinant
            elif sent[index][1] in ['nothing', 'everyone', 'anything', 'anyone'] and sent[index+1][1] in ['NN', 'NNS', 'NNP', 'NNPS', 'DT']:
                correct_text += 'but '
                error_count += 1
        correct_text += sent[-1][0]
    return error_count, textFormatter(correct_text)
