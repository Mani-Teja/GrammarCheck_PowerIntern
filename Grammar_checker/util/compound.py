"""Function built by Aviral Mishra for checking Compound Error i.e. if the words make a compound word together.
   eg 1:
        I/P:"Air" & "Bag"
        O/P:True
"""
import nltk
from nltk import word_tokenize
from util.readfile import read_file
def handleCompoundErrors(w1,w2):    
    path="resources/compounds.txt"
    text=read_file(path)
    compounds=[]
    for t in text:
        tokens=word_tokenize(t)
        word=tokens[0]+" "
        if tokens[1][-3:]=="was":
            word+=tokens[1][:-3]
        else:
            word+=tokens[1]
        compounds.append(word)
    w=w1+" "+w2
    if w in compounds:
        return True
    else:
        return False


