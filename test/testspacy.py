import spacy
from spacy import displacy



nlp = spacy.load('en')

doc = nlp("The paper describes a natural language based expert system route advisor for the public bus transport in Trondheim, Norway. The system is available on the Internet,and has been intstalled at the bus company web server since the beginning of 1999. The system is bilingual, relying on an internal language independent logic representation.")


# named entity recognition
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

# token analysis
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.is_stop)

# noun chunk extraction
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
          chunk.root.head.text)

# display dependency parser
options = {'compact': True, 'bg': '#09a3d5',
           'color': 'white', 'font': 'Source Sans Pro'}
displacy.serve(doc, style='dep', options=options)






