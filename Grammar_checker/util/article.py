from nltk.tokenize import word_tokenize
import nltk
from pattern.en import referenced

#Reading Text File by Chakori Chaturvedi 
def read_file(file):
    fp= open(file,"r",encoding='utf8',errors='ignore')
    text=fp.readlines()
    return text

"""Function build by Chakori Chaturvedi for checking article errors in a given sentence.
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
                #to check whether the (i)th word is in text file or tag of (i+1)th word is plural noun(eg cats,pencils) or proper noun,plural(eg Indians,Americans)
                if ((sent[i][0] in unc_words) or sent[i+1][1] in ["NNS" ,"NNPS"] ):
                    count+=1
                #to check whether the tag of(i+1)th word is adjective(large, fast, honest) and the tag of (i+2)th word is plural noun  
                elif (i<len(sent)-2) and (sent[i+1][1] in ["JJ","JJR"]) and (sent[i+2][1] in ['NNP','NN']):
                    """refernced provides appropriate article before the word 
                    eg:
                        I/P: referenced(hour)
                        O/P: an hour
                    """    
                    #to check whether (i)th word equals 'a'  and refernce of next word equals 'an '+(i+1)th word     
                    if (sent[i][0]=='a' and referenced(sent[i+1][0])==('an '+sent[i+1][0])):
                        ntext+='an'
                        count+=1
                    #to check whether (i)th word equals 'an'  and refernce of next word equals 'a '+(i+1)th word    
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
