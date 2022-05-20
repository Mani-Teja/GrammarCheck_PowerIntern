from grammarChecker.util import textFormatter


def check_becauseError(nlp):
    error_count = 0
    correct_text = ""
    for sent in nlp:
        for index in range(len(sent)):
            if sent[index][0] == 'because':
                # if condition for checking if the token encountered is punctuation
                if sent[index+1][1] == 'PUNCT' or index == len(sent)-1:
                    error_count += 1
                    correct_text += "."
                    break
                # if condition for checking if the token encountered is preposition
                if sent[index+1][1] == 'IN':
                    if index == len(sent)-2:
                        error_count += 1
                    # if condition for checking if the token encountered is not singular noun,plural noun,
                    # proper singular noun,proper plural noun,personal pronoun,possessive pronoun,determiner
                    elif sent[index + 2][1] not in ['NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$', 'DT']:
                        error_count += 1
                        correct_text += "."
                        break
                    else:
                        correct_text += sent[index][0]
                        correct_text += " "
                # if condition for checking if the token encountered is singular noun,plural noun,proper singular
                # noun,proper plural noun,personal pronoun,possessive pronoun
                elif sent[index + 1][1] in ['NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$']:
                    if index == len(sent)-2:
                        error_count += 1
                    flag = 0
                    for j in range(index + 2, len(sent)):
                        # if condition for checking if the token encountered is verb, modal
                        if sent[j][1] in ['VB', 'VBP', 'VBZ', 'VBG', 'VBN', 'VBD', 'MD']:
                            flag += 1
                            break
                    if flag == 0:
                        error_count += 1
                        correct_text += "."
                        break    
                    else:
                        correct_text += sent[index][0]
                        correct_text += " "
                else:
                    correct_text += sent[index][0]
                    correct_text += " "
            else:
                correct_text += sent[index][0]
                correct_text += " "
   
    return error_count, textFormatter(correct_text)
