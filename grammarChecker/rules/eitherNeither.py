from util.sentFormatter import textFormatter

def check_eitherneitherError(nlp):
    error_count=0
    correct_text=""
    word_count=0                    #stores the count of the word stored in variable word
    count_nor=0                     #stores the count of the occurance of word nor in a sentence
    word=""                         #stores a word i.e. either or neither
    for s in nlp:
        for i in range(len(s)):
            #print(s[i][0]+"**********"+s[i][1])
            if(i<len(s)-1) and word_count==1 and(s[i][1] in ['CC','RB']):              #condition for checking if there is an either neither present in the sentence and is the present word is a conjuction and adverb
                if(word=="either"):
                    error_count+=1
                    correct_text+="or "
                    word_count=0
                if(word=="neither"):
                    error_count+=1
                    correct_text+="nor "
                    word_count=0
                continue
            if(i<len(s)-1) and (s[i][0]=="either" or s[i][0]=="Either"):       #condition for checking if the word encountered is either
                word_count=1
                word="either"
                correct_text+=s[i][0]+" "
                continue
            if(i<len(s)-1) and (s[i][0]=="neither" or s[i][0]=="Neither"):     #condition for checking if the word encountered is neither
                word_count=1
                word="neither"
                correct_text+=s[i][0]+" "
                continue
            else:
                correct_text+=s[i][0]+" "
                if(s[i][0]=="nor"):                                            #condition for checking if the word encountered is nor
                    count_nor=1
        first_word = correct_text.split()[0]
        if(count_nor==1 and (first_word!="Neither" and first_word!="Either")):        #condition for checking if there is a nor present in the sentence without and neither or either as the first word.
            correct_text="Neither "+correct_text
    return error_count, textFormatter(correct_text)
