"""Function built by Sai Maniteja Penugonda for checking Capitalization Error
   eg 1:
        I/P:shyam is my friend.
        O/P:Shyam is my friend.
"""
from util.sentFormatter import textFormatter

def check_capitalization(nlp) :
    error_count = 0
    correct_text = ''
    punc = False
    for sent in nlp :
        for i in range(len(sent)) :
            # if condition for checking if tag encounterd is proposition or noun plural
            if i ==0 or sent[i][1] in ['PROPN' , 'NNS'] or punc:
                if punc :
                    punc = False
                #if condition for checking if token encountered is in lowercase  
                if sent[i][0].islower() :
                    error_count += 1
                    correct_text += sent[i][0].capitalize() + ' '
                else :
                    correct_text += sent[i][0] + ' '
            #if condition for checking if the token encountered is'i'           
            elif sent[i][0] == 'i' :
                error_count += 1
                correct_text += 'I '
            else :
                if sent[i][0] in '.,()[]{};:\'\"?!-' :
                    punc = True
                correct_text += sent[i][0]+' '
    return error_count , textFormatter(correct_text)
