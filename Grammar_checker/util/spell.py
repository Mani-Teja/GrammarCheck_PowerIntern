from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize

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
