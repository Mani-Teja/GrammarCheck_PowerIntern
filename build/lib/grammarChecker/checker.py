from grammarChecker.spell_check import spell_checker
from grammarChecker.rules.article import check_articleError
from grammarChecker.rules.capitalization import check_capitalization
from grammarChecker.rules.pluralization import check_pluralization
from grammarChecker.rules.subVerb import check_SubVerbAgreement
from grammarChecker.rules.Because import check_becauseError
from grammarChecker.rules.apostrophe import check_apostropheError
from grammarChecker.rules.andError import and_check
from grammarChecker.rules.tense import check_TenseError
from grammarChecker.rules.But import check_butError
from grammarChecker.rules.eitherNeither import check_eitherneitherError
from grammarChecker.rules.althoughthough import check_althoughthoughError
from grammarChecker.rules.reflexError import check_reflexError
from grammarChecker.util import base

# function for checking grammar errors
def check_grammar(data):
    err_count = 0
    # function call for spelling checker
    count, modified_text = spell_checker(data)
    err_count += count
    print('spell : ', modified_text)
    # function call for checking capitalization errors
    count, modified_text = check_capitalization(modified_text)
    err_count += count
    print('cap : ', modified_text)
    # function for checking apostrophe error
    count, modified_text = check_apostropheError(modified_text)
    err_count += count
    print('apostrophe :', modified_text)
    # function call for checking pluralization errors
    count, modified_text = check_pluralization(modified_text)
    err_count += count
    print('pluralization : ', modified_text)
    # function call for checking article errors
    count, modified_text = check_articleError(modified_text)
    err_count += count
    print('article : ', modified_text)
    # function call for checking subject Verb Agreement errors
    count, modified_text = check_SubVerbAgreement(modified_text)
    err_count += count
    print('sub-verb : ', modified_text)
    # function call for checking because error
    count, modified_text = check_becauseError(modified_text)
    err_count += count
    print('becoz : ', modified_text)
    # function call for checking but error
    count, modified_text = check_butError(modified_text)
    err_count += count
    print('but : ', modified_text)
    # function call for checking either-neither error
    count, modified_text = check_eitherneitherError(modified_text)
    err_count += count
    print('either-neither : ', modified_text)
    # function call for checking reflex pronoun error
    count, modified_text = check_reflexError(modified_text)
    err_count += count
    print('reflex pronoun : ', modified_text)
    # function call to check for and conjunction
    count, modified_text = and_check(modified_text)
    err_count += count
    print('and : ', modified_text)
    # function call to check for although-though error
    count, modified_text = check_althoughthoughError(modified_text)
    err_count += count
    print('although-though : ', modified_text)
    # function call for checking tense errors
    count, modified_text = check_TenseError(modified_text)
    err_count += count
    print('tense : ', modified_text)
    return err_count, modified_text


data = input("enter sentence : ")
errors, text = check_grammar(data)
print('errors : ', errors)
print('modified text : \n', text)
