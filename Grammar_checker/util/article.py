from nltk.tokenize import word_tokenize
import nltk
from pattern.en import referenced

#Reading Text File
def read_file(file):
    fp= open(file,"r",encoding='utf8',errors='ignore')
    text=fp.readlines()
    return text

"""Function build for checking article errors in a given sentence.
   eg 1:-
         I/P:I ate a apple.
         O/P:I ate an apple.
"""
def check_articleError(nlp):
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
