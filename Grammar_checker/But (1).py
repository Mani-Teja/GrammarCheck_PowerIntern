from nltk.tokenize import word_tokenize , sent_tokenize
import spacy , nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
def but_check(nlp) :
    error_count = 0
    correct_text = ''
    for sent in nlp :
        print(sent)
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
    return error_count , correct_text


def check_grammar(data) :
    err_count = 0
    modified_text = ''
    c,modified_text = but_check([nltk.pos_tag(word_tokenize(data))])
    err_count += c
    return err_count , modified_text
data = input("enter sentence : ")
errors , text = check_grammar(data)
print('errors : ',errors)
print('modified text : \n',text)



