"""Function built by Aviral Mishra for checking Apostrophe Error.
   eg 1:
        I/P:mum and dads house
        O/P:mum and dad's house
   eg 2:
        I/P:theyre leaving tomorrow
        O/P:they're leaving tomorrow
"""
from util.compound import handleCompoundErrors
from nltk.stem import PorterStemmer
from util.sentFormatter import textFormatter


def check_apostropheError(nlp):
    error_count = 0
    q = 0
    t = 0
    correct_text = ""
    ps = PorterStemmer()
    suffixList = ["m", "re", "t", "s", "ll", "ve", "d"]      # List of suffixes
    for s in nlp:
        for i in range(len(s)):
            if (i<len(s)-1) and s[i][1] in ['NN', 'NNS', 'NNP', 'NNPS', 'VB']:            #if condition for checking the tagging of the current token
                rootword = ps.stem(s[i][0])
                if rootword != (s[i][0].lower()):
                    for j in suffixList:                                                 #a loop traversing through the suffixList
                        if s[i][0].endswith(j):
                            if s[i+1][1] in ['NN', 'NNS', 'NNP', 'NNPS', 'VBG', 'DT', 'JJ']:    #if condition for checking the tagging of the next token
                                status=handleCompoundErrors(s[i][0],s[i+1][0])
                                if status:
                                    correct_text += s[i][0]+" "
                                    q += 1
                                    break
                                else:
                                    error_count += 1
                                    x = s[i][0].find(j)
                                    correct_text += s[i][0][0:x]
                                    correct_text += "'"+j+" "
                                    t = t+1
                                    break
            if q == 0 and t == 0:
                correct_text += s[i][0]
                correct_text += " "
            q = 0
            t = 0
    return error_count, textFormatter(correct_text)


# print(apostropheError([pos_tag(word_tokenize("It will be so nice to go to the beach. I want to confirm on which day
# we are leaving! Are we planning to get there now? I can't wait to spend some time with you. Thanks!"))]))
