from util.sentFormatter import textFormatter

def check_butError(nlp) :
    error_count = 0
    correct_text = ''
    for sent in nlp :
        for i in range(len(sent)-1) :
            correct_text += sent[i][0] + ' '
            #if the token encountered is ','
            if sent[i][1] in [','] :
                if sent[i-1][1] in ['NN','NNP','NNS','NNPS'] and sent[i+1][1] in['NN','NNS','NNP','NNPS']:
                    correct_text+=' '
                else:
                    correct_text += 'but '
                    error_count += 1
            #if the token encountered is noun and the next token encountered is also noun, determinant    
            elif sent[i][1] in ['nothing','everyone','anything','anyone'] and sent[i+1][1] in ['NN','NNS','NNP','NNPS','DT']:
                correct_text += 'but '
                error_count += 1
        correct_text += sent[-1][0]
    return error_count , textFormatter(correct_text)
