"""Function built by Aviral Mishra for checking Apostrophe Error.
   eg 1:
        I/P:mum and dads house
        O/P:mum and dad's house
   eg 2:
        I/P:theyre leaving tomorrow
        O/P:they're leaving tomorrow


"""
from nltk import word_tokenize,pos_tag
from util.sentFormatter import textFormatter


def check_apostropheError(nlp):
    error_count = 0
    if_count = 0      #acts as a flag to check if the final if condition is executed successfully
    length = 0        #stores length of the suffix
    correct_text = ""
    prp_word=""       #stores the sliced possible preposition word
    suffixList = ["m", "re", "t", "s", "ll", "ve", "d"]
    for s in nlp:
        for i in range(len(s)):
            if (i<len(s)-1) and s[i][1] in ['WRB','MD','PRP','PRP$','VBZ','RB','NNP','VBP','NN','VBD','NNS','VB','JJ'] and s[i+1][1] in ['VBP','VBG','VBD','JJ','VB','NN','IN']:
                if(s[i][1]=="VBZ" and s[i+1][1]=="JJ"):             #special case of is(i's)
                    correct_text += s[i][0]+" "
                else:
                    for j in suffixList:                                #loop traversing through suffixList
                        if s[i][0].endswith(j):                         #checking if the token ends with a particular suffix
                            if(j=='t'):
                                if(s[i][0].endswith("nt")):                       #special case of nt
                                   length=len(j)
                                   prp_word=s[i][0][slice(-length)]               #slicing the suffix
                                   prp_word=pos_tag(word_tokenize(prp_word))
                                   if(prp_word[0][1] in ['VBP','VB','MD']):
                                       correct_text += prp_word[0][0]+"n'"+j+" "      #don't,can't,shouldn't
                                       error_count+= 1
                                       if_count=1
                                       break
                            length=len(j)                                        #length of the particular token
                            prp_word=s[i][0][slice(-length)]                     #slicing the suffix
                            prp_word=pos_tag(word_tokenize(prp_word))
                            if(prp_word[0][1] in ['PRP','NN']):
                                correct_text += prp_word[0][0]+"'"+j+" "
                                error_count+= 1
                                if_count=1
                                break
                    if(if_count==0):
                        correct_text += s[i][0]+" "
            else:
                correct_text += s[i][0]+" "
            if_count=0
    return error_count, textFormatter(correct_text)