import nltk
from util.spell import *
from util.article import *
from util.capitalization import *
from util.pluralization import *

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

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
