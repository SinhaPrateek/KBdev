import os
import spacy
from collections import OrderedDict
import math
from textblob import TextBlob as tb
from read_xml import Read_XML

################ https://stevenloria.com/tf-idf/

################## CHANGE THE DIRECTORY AS NEEDED ################################
nlp = spacy.load('en')
filedir = os.getcwd()+"/"+"files"+"/"+"test_directory"
corpus = open(os.getcwd()+"/"+"files"+"/"+'text_corpus.txt','w')
f = open(os.getcwd()+"/"+"files"+"/"+'topic_output.txt','w')


i = 0       ### this is for counting the number of files read
files = []  ### list of discarded files


documents = []   ### whole corpus made of abstracts for now (List od docs) ['A major obstacle','to the construction',...] i.e. [doc1,doc2,doc3]
for file in os.listdir(filedir):
    i = i+1
    try:
        read_xml_obj = Read_XML(filedir+"/"+file)
        if read_xml_obj.parseable() == "parseable":
            documents.append(tb(read_xml_obj.getAbstract())) # convert to TextBlob object before appending
            corpus.write(read_xml_obj.getAbstract()+"\n")    # writing to file text_corpus.txt
        else:
            files.append(file)
    except:
        print(file)



print(i)     ### printing count of total read files
print(files)   ## printing discarded files




###################### Above steps were to create a corpus of documents in format [doc1,doc2,.....] ,
###################### now we will use it to find tfidf scores of noun chunks produced from Spacy

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
    f.write(str(doc)+"\n")
    chunk_score_dict = {}
    text_spacy = nlp(str(doc))
    for chunk in text_spacy.noun_chunks:
        chunk_text_blob = tb(chunk.text)
        score = 0
        for word in chunk_text_blob.words:
            score = score + tfidf(word, doc, documents)
        # print(chunk.text + " : " + str(score))
        chunk_score_dict[score] = chunk.text
        # print("-----------------------")

    # chunk_score_tuple = [(k, v) for k, v in chunk_score_dict.items()]
    # chunk_score_tuple.sort()
    #
    # for item in chunk_score_tuple:
    #     print(str(item[0]) + " : " + str(item[1]))
    ordered = OrderedDict(sorted(chunk_score_dict.items()))
    for key, value in ordered.items():
        print("%s: %s" % (key, value))
        f.write("%s: %s \n" % (key, value))

    print("-----------------------")
    print("-----------------------")
    print("-----------------------")
    f.write("-----------------------"+ "\n")




