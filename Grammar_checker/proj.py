import nltk
from nltk import pos_tag,word_tokenize,sent_tokenize
from util.spell import spell_checker
from util.article import check_articleError
from util.capitalization import check_capitalization
from util.pluralization import check_pluralization
from util.subVerb import check_SubVerbAgreement
from util.Because import check_becauseError
from util.apostrophe import apostropheError
from util.andError import and_check
from util.tense import check_TenseError
from util.But import check_butError
from util.eitherNeither import check_eitherneitherError
from util.althoughthough import check_althoughthoughError
from util.reflexError import check_reflexError
from util.sentFormatter import textFormatter

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def tagger(data) :
    sents = sent_tokenize(data)
    tags = []
    for sent in sents :
        tags.append(pos_tag(word_tokenize(sent)))
    return tags

#function for checking grammer errors
def check_grammar(data) :
    err_count = 0
    #function call for spelling checker
    c,modified_text = spell_checker(data)
    err_count += c
    print('spell : ',modified_text)
    #function for checking apostrophe error
    c,modified_text = apostropheError(tagger(modified_text))
    err_count += c
    print('apostraphie :',modified_text)
    #function call for checking pluralization errors
    c,modified_text = check_pluralization(tagger(modified_text))
    err_count += c
    print('plur : ',modified_text)
    #function call for checking article errors
    c,modified_text = check_articleError(tagger(modified_text))
    err_count += c
    print('artic : ',modified_text)
    #function call for checking subject Verb Agreement errors
    c,modified_text = check_SubVerbAgreement(tagger(modified_text))
    err_count += c
    print('subver : ',modified_text)
    #function call for checking because error
    c,modified_text = check_becauseError(tagger(modified_text))
    err_count += c
    print('becoz : ',modified_text)
    #function call for checking but error
    c,modified_text = check_butError(tagger(modified_text))
    err_count += c
    print('but : ',modified_text)
    #function call for checking either-neither error
    c,modified_text = check_eitherneitherError(tagger(modified_text))
    err_count += c
    print('either-neither : ',modified_text)
    #function call for checking reflex pronoun error
    c,modified_text = check_reflexError(tagger(modified_text))
    err_count += c
    print('reflex pronoun : ',modified_text)
    #function call to check for and conjuction
    c,modified_text = and_check(tagger(modified_text))
    err_count += c
    print('and : ',modified_text)    
    #function call to check for although-though error
    c,modified_text = check_althoughthoughError(tagger(modified_text))
    err_count += c
    print('although-though : ',modified_text)
    #function call for checking capitalization errors
    c,modified_text = check_capitalization(tagger(modified_text))
    err_count += c
    print('cap : ',modified_text)
    #function call for checking tense errors
    c,modified_text = check_TenseError(tagger(modified_text))
    err_count += c
    print('tense : ',modified_text)
    return err_count ,modified_text

data = input("enter sentence : ")
errors , text = check_grammar(data)
print('errors : ',errors)
print('modified text : \n',text)
