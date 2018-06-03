import os
import xml.dom.minidom as minidom
import spacy

import math
from textblob import TextBlob as tb
################ https://stevenloria.com/tf-idf/

nlp = spacy.load('en')
filedir = os.getcwd()+"/"+"files"+"/"+"unzipped"
f = open('text_corpus.txt','w')


#get the data from elements
def getText(nodelist):                  # always need to pass a list of node elements
    rc = []
    for node in nodelist:               # nodelist - [<DOM Element: title at 0x105fc7340>], node - <DOM Element: title at 0x105fc7340>
        onenodelist = node.childNodes   # onenodelist - [<DOM Text node "'The Effici'...">] "childNodes convert single Element obj to a single list of Textnode"
        for onenode in onenodelist:
            if onenode.nodeType == node.TEXT_NODE:
                rc.append(onenode.data)
    return '|'.join(rc)

#parse xml to get abstract and save to documents list of TextBlob objects one element for each file's abstract for now, should include title also
def parseHeading(Elem):
    if Elem.getAttribute("name") == "ParsHed":
        title = Elem.getElementsByTagName("title")
        author = Elem.getElementsByTagName("author")
        abstract = Elem.getElementsByTagName("abstract")
        # print(getText(abstract))
        documents.append(tb(getText(abstract)))   # convert to TextBlob object before appending
        f.write(getText(abstract)+",")             # writing to file text_corpus.txt



i = 0
files = []
documents = []
for file in os.listdir(filedir):
    i = i+1
    try:
        doc = minidom.parse(filedir + "/" + file)
        Elems = doc.getElementsByTagName('algorithm')
        for Elem in Elems:
            if Elem.getAttribute("name") == "ParsHed":
                title = Elem.getElementsByTagName("title")
                if len(title) == 1:
                    # print(file)
                    # print("\n")
                    parseHeading(Elem)
                else:
                    files.append(file)    ### for discarding vague files
                    break
            parseHeading(Elem)
    except:
        print(file)


print(i)     ### rinting count of total read files
print(files)   ## printing discarded files
# print("-----------------------")
# print("-----------------------")
# print(documents)


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


for doc in documents:
    print(str(doc))
    text_spacy = nlp(str(doc))
    for chunk in text_spacy.noun_chunks:
        chunk_text_blob = tb(chunk.text)
        score = 0
        for word in chunk_text_blob.words:
            score = score + tfidf(word, doc, documents)
        print(chunk.text + " : " + str(score))
        print("-----------------------")
    print("-----------------------")
    print("-----------------------")
    print("-----------------------")


#
#
#
#
#
# for i, blob in enumerate(documents):
#     print("Top words in document {}".format(i + 1))
#     scores = {word: tfidf(word, blob, documents) for word in blob.words}
#     sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
#     for word, score in sorted_words[:3]:
#         print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))


