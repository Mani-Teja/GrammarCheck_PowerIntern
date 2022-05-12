def textFormatter(text) :
    formatter = ''
    for word in text.split() :
        if word[0].isalnum() and (len(formatter)>0 and formatter[-1] != "'"):
            formatter += ' '
        formatter += word
    if formatter[-1] != '.' :
        formatter += '.'
    print(text)
    return formatter

#print(textFormatter('I was listening to the new Run the Jewels album . It is mostly hardcore Hip hop and I ’ d heard about it through youtube Reviews online . Fantano scored it an 8 '))
