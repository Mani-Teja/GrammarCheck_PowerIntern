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
            if (i!=len(s)-1) and (s[i][1] in ['NN' , 'NNP','NNS' , 'NNPS']) and s[i-1][1] in ['CD']:          #if condition for checking if the token encountered has cardinal digit as a pervious token.
                continue
            if (i!=len(s)-1) and (s[i][1] in ['NN' , 'NNP']):                       #if condition for checking if the token encountered is singular noun or a singular pronoun.
                if s[i+1][1] in ['VB','VBP'] or s[i-1][1] in ['VB','VBP','JJ']:     #if condition for checking if the singular noun or pronoun encountered is being followed by a (verb or singular verb in present tense) or has a (verb or singular verb in present tense or adjective) as its previous token. 
                    count+=1
                    correct_text+=pluralize(s[i][0])+" "
                else:
                    correct_text+=s[i][0]+" "
            elif (i!=len(s)-1) and (s[i][1] in ['NNS' , 'NNPS']):         #if condition for checking if the token encountered is plural noun or a plural pronoun.
                if s[i+1][1] in ['VBZ','NNS'] or s[i-1][1] in ['DT']:     #if condition for checking if the plural noun or pronoun encountered is being followed by a (plural noun or singular verb in present tense in 3rd person) or has a (determiner) as its previous token. 
                    correct_text+=singularize(s[i][0])+" "
                else:
                    correct_text+=s[i][0]+" "
            elif  (i!=len(s)-1) and s[i][1] in ['CD']:         #if condition for checking if the token encountered is a cardinal digit.
                if s[i][0]=="1" or s[i][0]=="one":             #if condition for checking if the cardinal digit encountered is one(1).
                    if s[i+1][1] in ['NNS' , 'NNPS']:          #if condition for checking if the cardinal digit encountered is being followed by a plural noun or plural pronoun.
                        count+=1
                        correct_text+=s[i][0]+" "+singularize(s[i+1][0])+" "
                else:
                    if s[i+1][1] in ['NN' , 'NNP']:            #if condition for checking if the cardinal digit encountered is being followed by a singular noun or singular pronoun.
                        count+=1
                        correct_text+=s[i][0]+" "+pluralize(s[i+1][0])+" "
            else:
                correct_text+=s[i][0]+" "
    return count,correct_text
