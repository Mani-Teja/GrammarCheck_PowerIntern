from grammarChecker.util import textFormatter


def check_althoughthoughError(nlp):
    error_count = 0
    correct_text = ""
    though_count = 0  # stores the count of no. of occurances of Though in a sentence.
    although_count = 0  # stores the count of no. of occurances of Although in a sentence.
    yet_count = 0  # stores the count of no. of occurances of yet in a sentence.
    for sent in nlp:
        for index in range(len(sent)):
            if index < len(sent) - 1 and sent[index][0] == "Though":  # condition for checking if the word encountered is though
                though_count = 1
            if index < len(sent) - 1 and sent[index][0] == "Although":  # condition for checking if the word encountered is although
                although_count = 1
            if index < len(sent) - 1 and sent[index][0] == "yet":  # condition for checking if the word encountered is yet
                yet_count = 1
                if though_count == 0 and although_count == 1:
                    correct_text += ","
                    continue
            # condition for checking if there is a comma present in the sentence with though as the first word
            if index < len(sent) - 1 and sent[index][0] == "," and though_count == 1 and although_count == 0:
                correct_text += "yet "
                continue
            else:
                correct_text += sent[index][0] + " "
        # condition for checking if there is a yet present in the sentence without though or although as the first word of the sentence
        if though_count == 0 and although_count == 0 and yet_count == 1:
            correct_text = "Though " + correct_text
    return error_count, textFormatter(correct_text)
