"""Function built by Aviral Mishra for checking Apostrophe Error.
   eg 1:
        I/P:mum and dads house
        O/P:mum and dad's house
   eg 2:
        I/P:theyre leaving tomorrow
        O/P:they're leaving tomorrow
"""
import nltk
from util.compound import handleCompoundErrors

def apostropheError(nlp):
    error_count=0
    correct_text=""
    suffixList=["m","re","s","t","ll","ve","d"]      #List of suffixes
    for s in nlp:
        for i in range(len(s)):
            if (i<len(s)-1) and s[i][1] in ['NN','NNS','NNP','NNPS','VB']:            #if condition for checking the tagging of the current token
                for j in suffixList :                                                 #a loop traversing through the suffixList
                    if s[i][0].endswith(j):
                        if s[i+1][1] in ['NN','NNS','NNP','NNPS','VBG','DT','JJ','VBP']:    #if condition for checking the tagging of the next token
                            status=handleCompoundErrors(s[i][0],s[i+1][0])
                            if status==True:
                                correct_text+=s[i][0]+" "
                            else:
                                error_count+=1
                                x=s[i][0].find(j)
                                correct_text+=s[i][0][0:x]
                                correct_text+="'"+j+" "
                                break
                else:
                    correct_text+=s[i][0]
                    correct_text+=" "
                
            else:
                correct_text+=s[i][0]
                correct_text+=" "
    return error_count,correct_text
