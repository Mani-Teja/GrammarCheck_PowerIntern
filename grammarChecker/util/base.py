from pattern.en import conjugate
from nltk import download, data

try:
    data.find('tokenizers/punkt')
except LookupError:
    download('punkt')
try:
    data.find("taggers/averaged_perceptron_tagger")
except LookupError:
    download('averaged_perceptron_tagger')
try:
    data.find('corpora/omw-1.4')
except LookupError:
    download('omw-1.4')
try:
    conjugate('go', 'part')
except:
    pass
