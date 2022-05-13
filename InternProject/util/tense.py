from util.sentFormatter import textFormatter
from pattern.en import conjugate

def check_TenseError(nlp):
    error_count=0
    correct_text=""
    try :
        conjugate('go','part')
    except :
        pass
    for sent in nlp:
        dic={"VB":0,"VBP":0,"VBD":0,"VBZ":0,"VBN":0,"VBG":0,"MD":0}
        for i in range(len(sent)):
            try:
                #if condition for checking if the token encountered is modal(could,will)
                if sent[i][1] == "MD" :
                    if (i<len(sent)-1) and (sent[i+1][1] in ["VBZ",'VBP','VBN','VBG','VBD']):
                        #change verb to its base form
                        word_lemma = lemma(wordnet_tagged[i+1])
                        if sent[i+1][0]!=word_lemma:
                            sent[i+1][0]=word_lemma
                            error_count+=1
                        dic["VB"]+=1
                        dic["MD"]+=1
                    #if condition for checking if the word encountered is "be" and token encountered is verb    
                    if i<len(sent)-2 and sent[i+1][0]=="be" and (sent[i+2][1] in ["VB","VBP","VBZ","VBD"]):
                        #change verb to its base form
                        v=lemma(wordnet_tagged[i+2])
                        #change verb to its participle
                        vp=conjugate(sent[i+2][0],"part")
                        
                        if vp!=sent[i+2][0]:
                            p=(vp,sent[i+2][1])
                            sent[i+2]=p
                            error_count+=1
                        dic["VBG"]+=1
                        dic["MD"]+=1
                    #if condition for checking if the token encountered is verb    
                    elif i<len(sent)-2 and (sent[i+1][1] in ["VB","VBP"]) and (sent[i+2][1] in ["VB","VBP","VBZ","VBD","VBG"]):
                        #change verb to its base form
                        v=lemma(wordnet_tagged[i+2])
                        #change verb to its past participle
                        vp=conjugate(v,"ppart")
                        if vp!=sent[i+2][0]:
                            p=(vp,sent[i+2][0])
                            sent[i+2]=p
                            error_count+=1
                        dic["VBN"]+=1
                        dic["MD"]+=1
                    correct_text+=sent[i][0]+" "
                #if condition for checking if the token encountered is verb past tense    
                elif i<len(sent)-1 and sent[i][1]=="VBD":
                    #if condition if the token encountered is verb past participle
                    if sent[i][0].lower()=="had" and sent[i+1][1]!="VBN":
                        #change verb to its base form
                        v=lemma(wordnet_tagged[i+1])
                        #change verb to its past participle
                        vp=conjugate(sent[i+1][0],"ppart")
                        if vp!=sent[i+1][0]:
                            p=(vp,sent[i+1][0])
                            sent[i+1]=p
                            error_count+=1
                        dic["VBD"]+=1
                        dic["VBN"]+=1
                        correct_text+=sent[i][0]+" "
                    #if condition for checking if the token encountered is verb    
                    elif sent[i+1][1] in ["VB","VBP","VBZ","VBD","VBN"]:
                        #change verb to its base form
                        v=lemma(wordnet_tagged[i+1])
                        #change verb to its past participle
                        vp=conjugate(v,"part")
                        if vp!=sent[i+1][0]:
                            p=(vp,sent[i+1][0])
                            sent[i+1]=p
                            error_count+=1
                        dic["VBD"]+=1
                        dic["VBG"]+=1
                        correct_text+=sent[i][0]+" "
                    else:
                        correct_text+=sent[i][0]+" "
                elif sent[i][1] in ["VB","VBP",'VBZ']:
                    #if condition for checking if the token encountered is verb and the word encountered is "have","has"
                    if i<(len(sent)-1) and (sent[i][0] in ["has","have"]) and (sent[i+1][1] in ["VBZ","VBD","VB","VBP","VBG",'VBN']):
                        #change verb to its past participle
                        vp=conjugate(sent[i+1][0],"ppart")
                        if vp!=sent[i+1][0]:
                            p=(vp,sent[i+1][0])
                            sent[i+1]=p
                            error_count+=1
                        dic["VBN"]+=1
                        correct_text+=sent[i][0]+" "
                    #if condition for checking if the token encountered is verb and the word encountered is "is","am","are"    
                    elif i<(len(sent)-1) and (sent[i][0] in ["is","am","are"]) and (sent[i+1][1] in ["VBZ","VBD","VB","VBP"]):
                        #change verb to its past participle
                        vp=conjugate(sent[i+1][0],"part")
                        if vp!=sent[i+1][0]:
                            p=(vp,sent[i+1][0])
                            sent[i+1]=p
                            error_count+=1
                        dic["VBG"]+=1
                        correct_text+=sent[i][0]+" "
                    else:
                        correct_text+=sent[i][0]+" "
                else:
                    correct_text+=sent[i][0]+" "
            except :
                correct_text+=sent[i][0]+" "
    return error_count,textFormatter(correct_text)
