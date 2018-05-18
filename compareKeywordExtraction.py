import os
import xml.dom.minidom as minidom
import spacy
from rake_nltk import Rake


nlp = spacy.load('en')
filedir = os.getcwd()+"/"+"files"+"/"+"unzipped"

f = open('comparitive_Study.txt','w')



def getText(nodelist):                  # always need to pass a list of node elements
    rc = []
    for node in nodelist:               # nodelist - [<DOM Element: title at 0x105fc7340>], node - <DOM Element: title at 0x105fc7340>
        onenodelist = node.childNodes   # onenodelist - [<DOM Text node "'The Effici'...">] "childNodes convert single Element obj to a single list of Textnode"
        for onenode in onenodelist:
            if onenode.nodeType == node.TEXT_NODE:
                rc.append(onenode.data)
    return '|'.join(rc)

def parseCitations(Elem):
    if Elem.getAttribute("name") == "ParsCit":
        citations = Elem.getElementsByTagName('citation')
        j = 0
        for citation in citations:
            j = j + 1
            cit_authors = citation.getElementsByTagName('author')
            cit_title = citation.getElementsByTagName("title")
            date = citation.getElementsByTagName("date")
            f.write("\n")
            f.write(getText(cit_title))
            f.write("\n")
            f.write(getText(date))
            f.write("\n")
            f.write(getText(cit_authors))
        f.write(j)

def parseHeading(Elem):
    if Elem.getAttribute("name") == "ParsHed":
        title = Elem.getElementsByTagName("title")
        author = Elem.getElementsByTagName("author")
        abstract = Elem.getElementsByTagName("abstract")
        f.write("Title: " + getText(title)+"\n")
        # f.write("\n")
        # f.write(getText("Author names: " + author))
        #f.write("\n")
        f.write("Abstract: " + getText(abstract))
        f.write("\n")
        doc = nlp(getText(abstract))

        f.write("\n" + "NOUN CHUNKS from Spacy:" + "\n")
        for chunk in doc.noun_chunks:
            f.write(chunk.text + "  ," +  chunk.root.text + "  ," + chunk.root.dep_ + "  ," + chunk.root.head.text + "\n")
        # f.write("\n" + "POS:" + "\n")
        # for token in doc:
        #     f.write(token.text,token.pos_)
        f.write("-----------------------"+"\n")

        # Uses stopwords for english from NLTK, and all puntuation characters.
        r = Rake()

        r.extract_keywords_from_text(getText(abstract))
        f.write("\n" + "NOUN CHUNKS from RAKE:" + "\n")

        for word_segment in r.get_ranked_phrases_with_scores():
            f.write(str(word_segment[0])+","+str(word_segment[1])+"\n")  # To get keyword phrases ranked highest to lowest.

        f.write("-----------------------"+"\n")
        f.write("-----------------------"+"\n")





i = 0
files = []
for file in os.listdir(filedir):
    i = i+1
    try:
        doc = minidom.parse(filedir + "/" + file)
        Elems = doc.getElementsByTagName('algorithm')
        for Elem in Elems:
            if Elem.getAttribute("name") == "ParsHed":
                title = Elem.getElementsByTagName("title")
                if len(title) == 1:
                    f.write(file)
                    f.write("\n")
                    parseHeading(Elem)
                else:
                    files.append(file)
                    break
    except:
        print(file)
        # parseCitations(Elem)


print(i)

print(files)

f.close()
