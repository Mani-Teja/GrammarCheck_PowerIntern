from nltk.tokenize import word_tokenize , sent_tokenize
import nltk
from pattern.en import referenced

def read_file(file):
    fp= open(file,"r",encoding='utf8',errors='ignore')
    text=fp.readlines()
    return text

def check_articleError(nlp):
    print(nlp)
    path="uncNouns.txt"
    unc_text=read_file(path)
    unc_words=[]
    for i in unc_text:
        tokens=word_tokenize(i)
        unc_words.append(tokens[0].lower())
    count=0
    ntext=""
    for sent in nlp :
        for i in range(len(sent)) :
            if sent[i][0] in ['a','an']:
                if ((sent[i][0] in unc_words) or sent[i+1][1] in ["NNS" ,"NNPS"] ):
                    count+=1
                elif (i<len(sent)-2) and (sent[i+1][1] in ["JJ","JJR"]) and (sent[i+2][1] in ['NNP','NN']):
                    if (sent[i][0]=='a' and referenced(sent[i+1][0])==('an '+sent[i+1][0])):
                        ntext+='an'
                        count+=1
                    elif(sent[i][0]=='an' and referenced(sent[i+1][0])==('a '+sent[i+1][0])):
                        ntext+='a'
                        count+=1
                    else:
                        ntext+=sent[i][0]
                elif (sent[i+1][1] not in ["NNP","NN"] ):
                    count+=1
                elif(sent[i][0] =='a' and referenced(sent[i+1][0])==('an '+sent[i+1][0])):
                    ntext+='an'
                    count+=1
                elif(sent[i][0]=='an' and referenced(sent[i+1][0])==('a '+sent[i+1][0])):
                    ntext+='a'
                    count+=1
                else:
                    ntext+=sent[i][0]
                ntext+=" "
            else:
                ntext+=sent[i][0]
                ntext+=" "
    return count , ntext

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

def check_grammar(data) :
    err_count = 0
    modified_text = ''
    c,modified_text = check_articleError([nltk.pos_tag(word_tokenize(data))])
    err_count += c
    c,modified_text = check_capitalization([nltk.pos_tag(word_tokenize(modified_text))])
    err_count += c
    return err_count , modified_text

data = input("enter sentence : ")
errors , text = check_grammar(data)
print('errors : ',errors)
print('modified text : \n',text)
