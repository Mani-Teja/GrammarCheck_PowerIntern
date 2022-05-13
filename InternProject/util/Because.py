from util.sentFormatter import textFormatter

def check_becauseError(nlp):
    error_count=0
    correct_text=""
    for sent in nlp:
        for i in range(len(sent)):
            if sent[i][0]=='because':
                #if condition for checking if the token encountered is punctuation
                if sent[i+1][1]=='PUNCT' or i==len(sent)-1:
                    error_count+=1
                    correct_text+="."
                    break
                #if condition for checking if the token encountered is preposition
                if sent[i+1][1]=='IN':
                    if i==len(sent)-2:
                        error_count+=1
                    #if condition for checking if the token encountered is not singular noun,plural noun,proper singular noun,proper plural noun,personal pronoun,possessive pronoun,determiner    
                    elif(sent[i+2][1] not in ['NN','NNS','NNP','NNPS','PRP','PRP$','DT']):
                        error_count+=1
                        correct_text+="."
                        break
                    else:
                        correct_text+=sent[i][0]
                        correct_text+=" "
                #if condition for checking if the token encountered is singular noun,plural noun,proper singular noun,proper plural noun,personal pronoun,possessive pronoun        
                elif sent[i+1][1] in ['NN','NNS','NNP','NNPS','PRP','PRP$']:
                    if i==len(sent)-2:
                        error_count+=1
                    flag=0
                    for j in range(i+2,len(sent)):
                        #if condition for checking if the token encountered is verb, modal
                        if sent[j][1] in ['VB','VBP','VBZ','VBG','VBN','VBD','MD']:
                            flag+=1
                            break
                    if flag==0:
                        error_count+=1
                        correct_text+="."
                        break    
                    else:
                        correct_text+=sent[i][0]
                        correct_text+=" "
                else:
                    correct_text+=sent[i][0]
                    correct_text+=" "
            else:
                correct_text+=sent[i][0]
                correct_text+=" "
   
    return error_count,textFormatter(correct_text)
