from nltk.tokenize import word_tokenize , sent_tokenize
import nltk
from pattern.en import referenced
from spellchecker import SpellChecker
from pattern.text.en import pluralize, singularize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#written by aviral mishra
def check_pluralization(nlp):
    count=0
    correct_text=""
    for s in nlp:
        for i in range(len(s)):
            if (i!=len(s)-1) and (s[i][1] in ['NN' , 'NNP','NNS' , 'NNPS']) and s[i-1][1] in ['CD']:
                continue
            if (i!=len(s)-1) and (s[i][1] in ['NN' , 'NNP']):
                if s[i+1][1] in ['VB','VBP'] or s[i-1][1] in ['VB','VBP','JJ']:
                    count+=1
                    correct_text+=pluralize(s[i][0])+" "
                else:
                    correct_text+=s[i][0]+" "
            elif (i!=len(s)-1) and (s[i][1] in ['NNS' , 'NNPS']):
                if s[i+1][1] in ['VBZ','NNS'] or s[i-1][1] in ['DT']:
                    correct_text+=singularize(s[i][0])+" "
                else:
                    correct_text+=s[i][0]+" "
            elif  (i!=len(s)-1) and s[i][1] in ['CD']:
                if s[i][0]=="1" or s[i][0]=="one":
                    if s[i+1][1] in ['NNS' , 'NNPS']:
                        count+=1
                        correct_text+=s[i][0]+" "+singularize(s[i+1][0])+" "
                else:
                    if s[i+1][1] in ['NN' , 'NNP']:
                        count+=1
                        correct_text+=s[i][0]+" "+pluralize(s[i+1][0])+" "
            else:
                correct_text+=s[i][0]+" "
    return count,correct_text

def spell_checker(data):
    spell = SpellChecker()
    misspelled = word_tokenize(data)
    mispelled , err_count ="" , 0
    for word in misspelled:
        corr_word = spell.correction(word)
        if  word != corr_word and not word.isupper() and word not in ['.','"',"'",'?','!',':',';','(',')','[',']','{','}',',']:
            mispelled=mispelled+corr_word+" "
            err_count += 1
        else :
            mispelled += word + ' '
    return err_count,mispelled

#written by chakori chaturvedi
def read_file(file):
    fp= open(file,"r",encoding='utf8',errors='ignore')
    text=fp.readlines()
    return text

def check_articleError(nlp):
    path="uncNouns.txt"
    unc_text=read_file(path)
    unc_words=[]
    for i in unc_text:
        tokens=word_tokenize(i)
        unc_words.append(tokens[0].lower())
    count=0
    ntext=""
    for sent in nlp :
        for i in range(len(sent)) :
            if sent[i][0] in ['a','an']:
                if ((sent[i][0] in unc_words) or sent[i+1][1] in ["NNS" ,"NNPS"] ):
                    count+=1
                elif (i<len(sent)-2) and (sent[i+1][1] in ["JJ","JJR"]) and (sent[i+2][1] in ['NNP','NN']):
                    if (sent[i][0]=='a' and referenced(sent[i+1][0])==('an '+sent[i+1][0])):
                        ntext+='an'
                        count+=1
                    elif(sent[i][0]=='an' and referenced(sent[i+1][0])==('a '+sent[i+1][0])):
                        ntext+='a'
                        count+=1
                    else:
                        ntext+=sent[i][0]
                elif (sent[i+1][1] not in ["NNP","NN"] ):
                    count+=1
                elif(sent[i][0] =='a' and referenced(sent[i+1][0])==('an '+sent[i+1][0])):
                    ntext+='an'
                    count+=1
                elif(sent[i][0]=='an' and referenced(sent[i+1][0])==('a '+sent[i+1][0])):
                    ntext+='a'
                    count+=1
                else:
                    ntext+=sent[i][0]
                ntext+=" "
            else:
                ntext+=sent[i][0]
                ntext+=" "
    return count , ntext

#written by maniteja
def check_capitalization(nlp) :
    error_count = 0
    correct_text = ''
    punc = False
    for sent in nlp :
        for i in range(len(sent)) :
            if i ==0 or sent[i][1] in ['PROPN' , 'NNS'] or punc:
                if punc :
                    punc = False
                if sent[i][0].islower() :
                    error_count += 1
                    correct_text += sent[i][0].capitalize() + ' '
                else :
                    correct_text += sent[i][0] + ' '
            elif sent[i][0] == 'i' :
                error_count += 1
                correct_text += 'I '
            else :
                if sent[i][0] in '.,()[]{};:\'\"?!-' :
                    punc = True
                correct_text += sent[i][0].lower()+' '
    return error_count , correct_text

def check_grammar(data) :
    err_count = 0
    c,modified_text = spell_checker(data)
    err_count += c
    c,modified_text = check_pluralization([nltk.pos_tag(word_tokenize(modified_text))])
    err_count += c
    c,modified_text = check_articleError([nltk.pos_tag(word_tokenize(modified_text))])
    err_count += c
    c,modified_text = check_capitalization([nltk.pos_tag(word_tokenize(modified_text))])
    err_count += c
    return err_count , modified_text

data = input("enter sentence : ")
errors , text = check_grammar(data)
print('errors : ',errors)
print('modified text : \n',text)
