from util.sentFormatter import textFormatter

def check_althoughthoughError(nlp):
    error_count=0
    correct_text=""
    th=0
    ath=0
    yet=0
    for s in nlp:
        for i in range(len(s)):
            if(i<len(s)-1 and s[i][0]=="Though"):           #condition for checking if the word encountered is though
                th=1
            if(i<len(s)-1 and s[i][0]=="Although"):         #condition for checking if the word encountered is although
                ath=1
            if(i<len(s)-1 and s[i][0]=="yet"):              #condition for checking if the word encountered is yet
                yet=1
                if(th==0 and ath==1):
                    correct_text+=","
                    continue
            if(i<len(s)-1 and s[i][0]=="," and th==1 and ath==0):    #condition for checking if there is a comma present in the sentence with though as the first word
                correct_text+="yet "
                continue
            else:
                correct_text+=s[i][0]+" "
        if(th==0 and ath==0 and yet==1):                    #condition for checking if there is a yet present in the sentence without though or although as the first word of the sentence
            correct_text="Though "+correct_text
    return error_count,textFormatter(correct_text)
