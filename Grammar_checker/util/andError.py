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
    return error_count , correct_text
#print(and_check([[('ajay', 'NN'), ('vijay', 'NN'), ('are', 'VBP'), ('friends', 'NNS')]]))
