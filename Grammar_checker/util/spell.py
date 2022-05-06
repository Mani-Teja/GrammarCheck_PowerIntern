from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize

"""This function is built by Aviral Mishra for checking any spelling errors.
   I/P:amazing spiderman is out in theators.
   O/P:Amazing spiderman is out in theaters.
"""
def spell_checker(data):
    spell = SpellChecker()
    misspelled = word_tokenize(data)
    mispelled , err_count ="" , 0
    for word in misspelled:
        corr_word = spell.correction(word)     #correcting spelling error
        if  word != corr_word and not word.isupper() and word[0] not in ['.','"',"'",'?','!',':',';','(',')','[',']','{','}',',']:   #if condition for checking if token is not in uppercase or any for the following punctuation marks.
            mispelled=mispelled+corr_word+" "
            err_count += 1
        else :
            if word[0] == "'" :
                mispelled = mispelled[:len(mispelled)-1]
            mispelled += word + ' '
    return err_count,mispelled
