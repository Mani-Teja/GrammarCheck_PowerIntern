'''
Method developed by Sai maniteja Penugonda

functionality : To check and modify the usage of reflex pronoun related errors provided in text.
i/p : andrew and myself will conduct todays meet
o/p : andrew and I will conduct todays meet

'''

from grammarChecker.util import textFormatter


def check_reflexError(nlp):
    correct_text = ''
    error_count = 0
    for sent in nlp:
        # reflex pronoun can't be used at beginning of sentence.
        if sent[0][1] == 'PRP':
            if sent[0][0].startswith('my'):
                correct_text += 'I am '
            elif sent[0][0].startswith('our'):
                correct_text += 'we are '
            elif sent[0][0].startswith('him'):
                correct_text += 'he is '
            elif sent[0][0].startswith('her'):
                correct_text += 'she is '
            elif sent[0][0].startswith('them'):
                correct_text += 'they are '
            else:
                correct_text += sent[0][0] + ' '
        if len(correct_text) == 0:
            correct_text += sent[0][0] + ' '
        for i in range(1, len(sent)):
            # reflex pronoun cant be used with compound subject or compound object
            if sent[i][1] == 'PRP' and 'sel' in sent[i][0] and sent[i - 1][1] == 'CC':
                error_count += 1
                if sent[i][0].startswith('my'):
                    if i < len(sent) / 2:
                        correct_text += 'I '
                    else:
                        correct_text += 'me '
                elif sent[i][0].startswith('our'):
                    if i < len(sent) / 2:
                        correct_text += 'we '
                    else:
                        correct_text += 'us '
                elif sent[i][0].startswith('him'):
                    if i < len(sent) / 2:
                        correct_text += 'he '
                    else:
                        correct_text += 'him '
                elif sent[i][0].startswith('her'):
                    if i < len(sent) / 2:
                        correct_text += 'she '
                    else:
                        correct_text += 'her '
                elif sent[i][0].startswith('them'):
                    if i < len(sent) / 2:
                        correct_text += 'they '
                    else:
                        correct_text += 'them '
            else:
                correct_text += sent[i][0] + ' '
    return error_count, textFormatter(correct_text)
