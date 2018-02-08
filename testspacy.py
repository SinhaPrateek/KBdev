import spacy
from spacy import displacy
import os
from lxml import etree
import xml.dom.minidom as minidom

"""
nlp = spacy.load('en')

doc = nlp("The paper describes a natural language based expert system route advisor for the public bus transport in Trondheim, Norway. The system is available on the Internet,and has been intstalled at the bus company web server since the beginning of 1999. The system is bilingual, relying on an internal language independent logic representation.")


for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.is_stop)
"""
"""
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
          chunk.root.head.text)
"""

"""
options = {'compact': True, 'bg': '#09a3d5',
           'color': 'white', 'font': 'Source Sans Pro'}
displacy.serve(doc, style='dep', options=options)

"""
i = 0
for filename in os.listdir(os.getcwd()):
    if filename == "A":
        for filname in os.listdir(os.getcwd() + "/" + filename):
            if filname == "A00":
                for file in os.listdir(os.getcwd() + "/" + filename + "/" + filname):
                    i = i+1
                    if (i!=1 & i<4):
                        doc = minidom.parse(os.getcwd() + "/" + filename + "/" + filname+ "/" + file)
                        Elem = doc.getElementsByTagName('sectionHeader')[0]
                        print("Text : ", Elem.firstChild.nodeValue)
                    else:
                        break





