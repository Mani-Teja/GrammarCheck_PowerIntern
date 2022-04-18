import nltk

"""Function built for checking Capitalization Error
   eg 1:
        I/P:shyam is a friend.
        O/P:Shyam is a friend.
"""
def check_capitalization(nlp) :
    error_count = 0
    correct_text = ''
    punc = False
    for sent in nlp :
        for i in range(len(sent)) :
            if i ==0 or sent[i][1] in ['PROPN' , 'NNS'] or punc:
                if punc :
                    punc = False
                if sent[i][0].islower() :
                    error_count += 1
                    correct_text += sent[i][0].capitalize() + ' '
                else :
                    correct_text += sent[i][0] + ' '
            elif sent[i][0] == 'i' :
                error_count += 1
                correct_text += 'I '
            else :
                if sent[i][0] in '.,()[]{};:\'\"?!-' :
                    punc = True
                correct_text += sent[i][0].lower()+' '
    return error_count , correct_text
