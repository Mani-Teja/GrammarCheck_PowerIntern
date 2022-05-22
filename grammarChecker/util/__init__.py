def textFormatter(text):
    formatter = ''
    for word in text.split():
        if word[0].isalnum() and (len(formatter) > 0 and formatter[-1] != "'"):
            formatter += ' '
        formatter += word
    if formatter[-1] != '.':
        formatter += '.'
    return formatter
