from util.sentFormatter import textFormatter

def check_eitherneitherError(nlp):
    error_count=0
    correct_text=""
    dt=0
    cn=0
    dtname=""
    for s in nlp:
        for i in range(len(s)):
            if(i<len(s)-1) and dt==1 and(s[i][1] in ['CC','RB']):              #condition for checking if there is an either neither present in the sentence and is the present word is a conjuction and adverb
                if(dtname=="either"):
                    error_count+=1
                    correct_text+="or "
                    dt=0
                if(dtname=="neither"):
                    error_count+=1
                    correct_text+="nor "
                    dt=0
                continue
            if(i<len(s)-1) and (s[i][0]=="either" or s[i][0]=="Either"):       #condition for checking if the word encountered is either
                dt=1
                dtname="either"
                correct_text+=s[i][0]+" "
                continue
            if(i<len(s)-1) and (s[i][0]=="neither" or s[i][0]=="Neither"):     #condition for checking if the word encountered is neither
                dt=1
                dtname="neither"
                correct_text+=s[i][0]+" "
                continue
            else:
                correct_text+=s[i][0]+" "
                if(s[i][0]=="nor"):                                            #condition for checking if the word encountered is nor
                    cn=1
        first_word = correct_text.split()[0]
        if(cn==1 and (first_word!="Neither" and first_word!="Either")):        #condition for checking if there is a nor present in the sentence without and neither or either as the first word.
            correct_text="Neither "+correct_text
    return error_count, textFormatter(correct_text)
