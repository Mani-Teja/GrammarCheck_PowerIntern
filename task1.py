#task-1
import spacy
from nltk import Tree
nlp = spacy.load("en_core_web_sm")
doc = nlp(input("eneter sentence : "))
variable = input("enter variable ; ").lower()
result = {}

def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        childs = ''.join([c.text.lower() for c in node.children])
        if node.pos_ == 'VERB' :
            result[node.text] = variable in childs
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_


x = [to_nltk_tree(sent.root) for sent in doc.sents]
#x[0].pretty_print()
for verb in x :
    verb.pretty_print()

for i in result :
    print(result[i])
