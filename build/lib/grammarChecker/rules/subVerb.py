"""
Method developed by Sai maniteja Penugonda

functionality : To check and modify the Subject Verb agreement related errors provided in text.
i/p Parameters : list of tuples [[word , pos_tag],...]
o/p : (int , string) -> (error count , correct text)
"""

from pattern.en import conjugate
from grammarChecker.util import *


def check_SubVerbAgreement(text):
    nlp = tagger(text)
    count = 0
    text = ""
    for sent in nlp:
        for index in range(len(sent)):
            if "'" in sent[index][0] or (index < len(sent)-1 and "'" in sent[index+1][0]):
                text += sent[index][0] + ' '
                continue
            try:
                if sent[index][1] in ['NN', 'NNP']:
                    # condition to check the next word is VERB
                    if index != len(sent)-1 and sent[index+1][1] in ['VB', 'VBP', 'VBG']:
                        conj = conjugate(sent[index+1][0], tense="present", person=3, number="singular", mood="indicative", aspect="imperfective", negated=False)
                        text += sent[index][0]+" "
                        if sent[index+1][0] != conj:
                            sent[index+1] = (conj, sent[index+1][1])
                            count += 1
                        text += " "
                    # condition to check the next word is NOUN
                    elif index != len(sent)-1 and sent[index+1][1] in ['NN', 'NNP']:
                        conj = conjugate(sent[index+1][0], tense='present', person=3, number='singular', mood='indicative', aspect='imperfective', negated=False)
                        text += sent[index][0]+" "
                        if sent[index+1][0] != conj:
                            sent[index+1] = (conj, sent[index+1][1])
                            count += 1
                        text += " "
                    else:
                        text += sent[index][0] + ' '
                # condition to check the current word id PLURAL NOUN
                elif index != len(sent)-1 and sent[index][1] in ['NNS', 'NNPS']:
                    # condition to check the next word is VERB (present participle / 3rd person singular)
                    if sent[index+1][1] in ['VBG', 'VBZ']:
                        conj = conjugate(sent[index+1][0], tense="present", person=3, number="plural", mood="indicative", aspect="imperfective", negated=False)
                        text += sent[index][0]+" "
                        if sent[index+1][0] != conj:
                            sent[index+1] = (conj,sent[index+1][1])
                            count += 1
                        text += " "
                    else:
                        text += sent[index][0]+" "
                # condition to check current word is PERSONAL PRONOUN
                elif index != len(sent)-1 and sent[index][1] == 'PRP':
                    if sent[index][0] == 'I':
                        # condition to check the next word is VERB (present participle/ past participle / 3rd person singular)
                        if sent[index+1][1] in ['VBZ', 'VBN', 'VBG']:
                            conj = conjugate(sent[index+1][0], tense="present", person=1, number="singular", mood="indicative", aspect="imperfective", negated=False)
                            text += sent[index][0]+" "
                            if sent[index+1][0] != conj:
                                sent[index+1] = (conj, sent[index+1][1])
                                count += 1
                            text += " "
                        else:
                            text += sent[index][0]
                            text += " "
                    elif sent[index][0].lower() in ['he', 'she', 'it']:
                        if sent[index+1][1] in ['VBP', 'VB', 'VBN', 'VBG']:
                            conj = conjugate(sent[index+1][0], tense="present", person=3, number="singular", mood="indicative", aspect="imperfective", negated=False)
                            text += sent[index][0]+" "
                            if sent[index+1][0] != conj:
                                sent[index+1] = (conj, sent[index+1][1])
                                count += 1
                            text += " "
                        else:
                            text += sent[index][0]+" "
                    elif sent[index][0].lower() in ['we', 'they', 'you']:
                        if sent[index+1][1] not in ['VB', 'VBP']:
                            conj = conjugate(sent[index+1][0], tense="present", person=3, number="plural", mood="indicative", aspect="imperfective", negated=False)
                            text += sent[index][0]+" "
                            if sent[index+1][0] != conj:
                                sent[index+1] = (conj, sent[index+1][1])
                                count += 1
                            text += " "
                        else:
                            text += sent[index][0]
                            text += " "
                    else:
                        text += sent[index][0]+" "
                else:
                    text += sent[index][0]+" "
            except:
                pass
    return count, textFormatter(text)
