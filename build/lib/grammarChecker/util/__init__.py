from nltk import sent_tokenize, word_tokenize, pos_tag


def textFormatter(text):
    formatter = ''
    for word in text.split():
        if word[0].isalnum() and (len(formatter) > 0 and formatter[-1] != "'"):
            formatter += ' '
        formatter += word
    if formatter[-1] != '.':
        formatter += '.'
    return formatter


def tagger(data):
    sents = sent_tokenize(data)
    tags = []
    for sent in sents:
        tags.append(pos_tag(word_tokenize(sent)))
    return tags
