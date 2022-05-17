'''
This method developed by Maniteja.
This method helps to format the given sentence into the readable format which doesn't have any indentation issues.
extra spaces at the Head and Tail of the sentences and irregular spaces in between the sentence are eliminated.

'''
def textFormatter(text) :
    formatter = ''
    for word in text.split() :
        if word[0].isalnum() and (len(formatter)>0 and formatter[-1] != "'"):
            formatter += ' '
        formatter += word
    if formatter[-1] != '.' :
        formatter += '.'
    return formatter
