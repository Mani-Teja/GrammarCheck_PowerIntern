from pattern.en import conjugate
from grammarChecker.util import textFormatter


def check_TenseError(nlp):
    error_count = 0
    correct_text = ""
    try:
        conjugate('go', 'part')
    except:
        pass
    for sent in nlp:
        dic = {"VB": 0, "VBP": 0, "VBD": 0, "VBZ": 0, "VBN": 0, "VBG": 0, "MD": 0}
        for index in range(len(sent)):
            try:
                # if condition for checking if the token encountered is modal(could,will)
                if sent[index][1] == "MD":
                    if index < len(sent) - 1 and sent[index + 1][1] in ["VBZ", 'VBP', 'VBN', 'VBG', 'VBD']:
                        # change verb to its base form
                        word_lemma = lemma(wordnet_tagged[index + 1])
                        if sent[index + 1][0] != word_lemma:
                            sent[index + 1][0] = word_lemma
                            error_count += 1
                        dic["VB"] += 1
                        dic["MD"] += 1
                    # if condition for checking if the word encountered is "be" and token encountered is verb
                    if index < len(sent) - 2 and sent[index + 1][0] == "be" and sent[index + 2][1] in ["VB", "VBP", "VBZ", "VBD"]:
                        # change verb to its participle
                        participle = conjugate(sent[index + 2][0], "part")
                        if participle != sent[index + 2][0]:
                            correct_word = (participle, sent[index + 2][1])
                            sent[index + 2] = correct_word
                            error_count += 1
                        dic["VBG"] += 1
                        dic["MD"] += 1
                    # if condition for checking if the token encountered is verb
                    elif index < len(sent) - 2 and sent[index + 1][1] in ["VB", "VBP"] \
                            and sent[index + 2][1] in ["VB", "VBP", "VBZ", "VBD", "VBG"]:
                        # change verb to its base form
                        verb = lemma(wordnet_tagged[index + 2])
                        # change verb to its past participle
                        participle = conjugate(verb, "ppart")
                        if participle != sent[index + 2][0]:
                            correct_word = (participle, sent[index + 2][0])
                            sent[index + 2] = correct_word
                            error_count += 1
                        dic["VBN"] += 1
                        dic["MD"] += 1
                    correct_text += sent[index][0] + " "
                # if condition for checking if the token encountered is verb past tense
                elif index < len(sent) - 1 and sent[index][1] == "VBD":
                    # if condition if the token encountered is verb past participle
                    if sent[index][0].lower() == "had" and sent[index + 1][1] != "VBN":
                        # change verb to its past participle
                        participle = conjugate(sent[index + 1][0], "ppart")
                        if participle != sent[index + 1][0]:
                            correct_word = (participle, sent[index + 1][0])
                            sent[index + 1] = correct_word
                            error_count += 1
                        dic["VBD"] += 1
                        dic["VBN"] += 1
                        correct_text += sent[index][0] + " "
                    # if condition for checking if the token encountered is verb
                    elif sent[index + 1][1] in ["VB", "VBP", "VBZ", "VBD", "VBN"]:
                        # change verb to its base form
                        verb = lemma(wordnet_tagged[index + 1])
                        # change verb to its past participle
                        participle = conjugate(verb, "part")
                        if participle != sent[index + 1][0]:
                            correct_word = (participle, sent[index + 1][0])
                            sent[index + 1] = correct_word
                            error_count += 1
                        dic["VBD"] += 1
                        dic["VBG"] += 1
                        correct_text += sent[index][0] + " "
                    else:
                        correct_text += sent[index][0] + " "
                elif sent[index][1] in ["VB", "VBP", 'VBZ']:
                    # if condition for checking if the token encountered is verb and the word encountered is "have","has"
                    if index < (len(sent) - 1) and sent[index][0] in ["has", "have"] and sent[index + 1][1] in ["VBZ", "VBD", "VB", "VBP", "VBG", 'VBN']:
                        # change verb to its past participle
                        participle = conjugate(sent[index + 1][0], "ppart")
                        if participle != sent[index + 1][0]:
                            correct_word = (participle, sent[index + 1][0])
                            sent[index + 1] = correct_word
                            error_count += 1
                        dic["VBN"] += 1
                        correct_text += sent[index][0] + " "
                    # if condition for checking if the token encountered is verb and the word encountered is "is","am","are"
                    elif index < (len(sent) - 1) and (sent[index][0] in ["is", "am", "are"]) and (sent[index + 1][1] in ["VBZ", "VBD", "VB", "VBP"]):
                        # change verb to its past participle
                        participle = conjugate(sent[index + 1][0], "part")
                        if participle != sent[index + 1][0]:
                            correct_word = (participle, sent[index + 1][0])
                            sent[index + 1] = correct_word
                            error_count += 1
                        dic["VBG"] += 1
                        correct_text += sent[index][0] + " "
                    else:
                        correct_text += sent[index][0] + " "
                else:
                    correct_text += sent[index][0] + " "
            except:
                correct_text += sent[index][0] + " "
    return error_count, textFormatter(correct_text)
