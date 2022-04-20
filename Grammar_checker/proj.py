import nltk
from nltk import pos_tag,word_tokenize
from util.spell import spell_checker
from util.article import check_articleError
from util.capitalization import check_capitalization
from util.pluralization import check_pluralization
from util.readfile import read_file
from util.subVerb import check_SubVerbAgreement
from util.Because import check_becauseError
from util.apostrophe import apostropheError

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


#function for checking grammer errors
def check_grammar(data) :
    err_count = 0
    #function call for spelling checker
    c,modified_text = spell_checker(data)
    err_count += c
    #function call for checking pluralization errors
    c,modified_text = check_pluralization([nltk.pos_tag(word_tokenize(modified_text))])
    err_count += c
    #function for checking apostrophe error
    c,modified_text = apostropheError([nltk.pos_tag(word_tokenize(modified_text))])
    err_count += c
    path="resources/uncNouns.txt"
    unc_text=read_file(path)
    #function call for checking article errors
    c,modified_text = check_articleError([nltk.pos_tag(word_tokenize(modified_text))],unc_text)
    err_count += c
    #function call for checking subject Verb Agreement errors
    #c,modified_text = check_SubVerbAgreement([nltk.pos_tag(word_tokenize(modified_text))])
    #err_count += c
    #function call for checking because error
    c,modified_text = check_becauseError([nltk.pos_tag(word_tokenize(modified_text))])
    err_count += c
    #function call for checking capitalization errors
    c,modified_text = check_capitalization([nltk.pos_tag(word_tokenize(modified_text))])
    err_count += c
    return err_count , modified_text

data = input("enter sentence : ")
errors , text = check_grammar(data)
print('errors : ',errors)
print('modified text : \n',text)
