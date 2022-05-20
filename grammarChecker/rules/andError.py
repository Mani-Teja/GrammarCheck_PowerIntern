"""Function build by maniteja for checking usage of AND conjuction in a given sentence.
   eg 1:-
         I/P: ajay vijay are friends
         O/P: ajay and vijay are friends
"""
from util.sentFormatter import textFormatter

def and_check(nlp) :
    error_count = 0
    correct_text = ''
    for sent in nlp :
        for i in range(len(sent)-1) :
            #print(sent[i][0] , sent[i][1])
            correct_text += sent[i][0] + ' '
            if sent[i][1][0] in ['N','J','V'] :
                if sent[i][1] == sent[i+1][1] :
                    correct_text += 'and '
                    error_count += 1
        correct_text += sent[-1][0]
    return error_count , textFormatter(correct_text)

#print(and_check([[('ajay', 'NN'), ('vijay', 'NN'), ('are', 'VBP'), ('friends', 'NNS')]]))
