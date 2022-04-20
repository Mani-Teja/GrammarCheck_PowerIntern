'''
Method developed by Sai maniteja Penugonda

functionality : To check and modify the Subject Verb aggrement related errors provided in text.
i/p Parameters : list of 2d matrix [[word , pos_tag],...]
o/p : (int , string) -> (error count , correct text)
'''

from pattern.en import conjugate
import nltk
from nltk.stem import WordNetLemmatizer

def check_SubVerbAgreement(nlp):
    count=0
    text=""
    lemmatizer= WordNetLemmatizer()
    for s in nlp:
        for i in range(len(s)):
            try:
                if s[i][1] in [ 'NN' , 'NNP'] :
                    #condition to check the next word is VERB
                    if (i!=len(s)-1) and (s[i+1][1] in ['VB','VBP','VBG']):
                        verbLemma=lemmatizer.lemmatize(s[i+1][0])
                        v=conjugate(verbLemma, tense = "present",person = 3, number = "singular", mood = "indicative",aspect = "imperfective",negated = False)
                        text+=s[i][0]+" "
                        if s[i+1][0] != v :
                            count+=1
                            s[i+1][0] = v
                        text += " "
                    # condition to check the next word is NOUN
                    elif (i!=len(s)-1) and (s[i+1][1] in ['NN','NNP']):
                        verbLemma=lemmatizer.lemmatize(s[i+1][0])
                        v=conjugate(verbLemma,tense = 'present' , person = 3 , number = 'singular' , mood = 'indicative' , aspect = 'imperfective' , negated = False)
                        text+=s[i][0]+" "
                        if s[i+1][0] != v :
                            count+=1
                            s[i+1][0] = v
                        text += " "
                    else:
                        text+=s[i][0]
                        text+=" "
                #condition to check the current word id PLURAL NOUN
                elif (i!=len(s)-1) and (s[i][1] in ['NNS' , 'NNPS']):
                    #condition to check the next word is VERB (present participle / 3rd person singular)
                    if s[i+1][1] in ['VBG','VBZ']:
                        verbLemma=lemmatizer.lemmatize(s[i+1][0])
                        v=conjugate(verbLemma, tense = "present",person = 3, number = "plural", mood = "indicative",aspect = "imperfective",negated = False)
                        text+=s[i][0]+" "
                        if s[i+1][0] != v:
                            count+=1
                            s[i+1][0]=v
                        text+=" "
                    else:
                        text+=s[i][0]
                        text+=" "
                #condition to check current word is PERSONAL PRONOUN
                elif (i!=len(s)-1) and s[i][1] == 'PRP':
                    if s[i][0] == 'I':
                        #condition to check the next word is VERB (present participle/ past participle / 3rd person singular)
                        if s[i+1][1] in ['VBZ','VBN','VBG']:                            
                            verbLemma=lemmatizer.lemmatize(s[i+1][0])
                            v=conjugate(verbLemma, tense = "present",person = 1, number = "singular", mood = "indicative",aspect = "imperfective",negated = False)
                            text+=s[i][0]+" "
                            if s[i+1][0]!=v:
                                count+=1
                                s[i+1][0]=v
                            text+=" "
                        else:
                            text+=s[i][0]
                            text+=" "
                    elif s[i][0].lower() in ['he','she','it']:
                        if s[i+1][1] in ['VBP','VB','VBN','VBG']:
                            verbLemma=lemmatizer.lemmatize(s[i+1][0])
                            v=conjugate(verbLemma, tense = "present",person = 3, number = "singular", mood = "indicative",aspect = "imperfective",negated = False)
                            text+=s[i][0]+" "
                            if s[i+1][0] !=v:
                                count+=1
                                s[i+1][0] =v
                            text+=" "
                        else:
                            text+=s[i][0]
                            text+=" "
                    elif s[i][0].lower() in ['we','they','you']:
                        if s[i+1][1] not in ['VB','VBP']:
                            verbLemma=lemmatizer.lemmatize(s[i+1][0])
                            v=conjugate(verbLemma, tense = "present",person = 3, number = "plural", mood = "indicative",aspect = "imperfective",negated = False)
                            text+=s[i][0]+" "
                            if s[i+1][0] !=v:
                                count+=1
                                s[i+1][0]=v
                            text+=" "
                        else:
                            text+=s[i][0]
                            text+=" "
                    else:
                        text+=s[i][0]
                        text+=" "
                else:
                    text+=s[i][0]
                    text+=" "
            except Exception as e:
                text+=s[i][0]
                text+=" "
    return count,text
