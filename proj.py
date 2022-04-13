import spacy

doc = spacy.load("en_core_web_sm")
doc.add_pipe("merge_entities")
data = input("enter sentence : ")
doc.add_pipe("merge_noun_chunks")
for te in doc(data) :
    print(te.text , te.pos_)
