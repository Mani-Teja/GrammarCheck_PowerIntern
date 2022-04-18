import nltk
from pattern.text.en import pluralize, singularize

"""Function built by Aviral Mishra for checking Pluralization Error
   eg 1:
        I/P:there are many chocolate in the box.
        O/P:There are many chocolates in the box.
"""
def check_pluralization(nlp):
    count=0
    correct_text=""
    for s in nlp:
        for i in range(len(s)):
            if (i!=len(s)-1) and (s[i][1] in ['NN' , 'NNP','NNS' , 'NNPS']) and s[i-1][1] in ['CD']:
                continue
            if (i!=len(s)-1) and (s[i][1] in ['NN' , 'NNP']):
                if s[i+1][1] in ['VB','VBP'] or s[i-1][1] in ['VB','VBP','JJ']:
                    count+=1
                    correct_text+=pluralize(s[i][0])+" "
                else:
                    correct_text+=s[i][0]+" "
            elif (i!=len(s)-1) and (s[i][1] in ['NNS' , 'NNPS']):
                if s[i+1][1] in ['VBZ','NNS'] or s[i-1][1] in ['DT']:
                    correct_text+=singularize(s[i][0])+" "
                else:
                    correct_text+=s[i][0]+" "
            elif  (i!=len(s)-1) and s[i][1] in ['CD']:
                if s[i][0]=="1" or s[i][0]=="one":
                    if s[i+1][1] in ['NNS' , 'NNPS']:
                        count+=1
                        correct_text+=s[i][0]+" "+singularize(s[i+1][0])+" "
                else:
                    if s[i+1][1] in ['NN' , 'NNP']:
                        count+=1
                        correct_text+=s[i][0]+" "+pluralize(s[i+1][0])+" "
            else:
                correct_text+=s[i][0]+" "
    return count,correct_text
