#Reading Text File by Chakori Chaturvedi 
def read_file(file):
    fp= open(file, "r", encoding='utf8', errors='ignore')
    text=fp.readlines()
    return text


def textFormatter(text):
    formatter = ''
    for word in text.split():
        if word[0].isalnum() and (len(formatter) > 0 and formatter[-1] != "'"):
            formatter += ' '
        formatter += word
    if formatter[-1] != '.':
        formatter += '.'
    return formatter
