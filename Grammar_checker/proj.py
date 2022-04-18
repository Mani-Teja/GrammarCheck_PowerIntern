import nltk
from nltk import pos_tag,word_tokenize
from util.spell import spell_checker
from util.article import check_articleError
from util.capitalization import check_capitalization
from util.pluralization import check_pluralization

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
