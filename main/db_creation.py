import os
import pickle
import tarfile

import math
from collections import OrderedDict
import spacy
from textblob import TextBlob as tb

from main.classFiles import Paper
from main.read_xml import Read_XML

filedir = os.getcwd()+ "/" + "files" + "/" + "archives/acl-arc-160301-parscit"
unzipped_dir = os.getcwd()+ "/" + "files" + "/" + "unzipped"
flattened_files_dir = os.getcwd()+ "/" + "files" + "/" + "flattened_unzipped"
intermediate_output_file = open(os.getcwd()+ "/" + "files" + "/intermediate_output.txt",'w')
Title_dict_pickle = open(os.getcwd()+ "/" + "files" + "/title_dict.pickle",'wb')
Author_dict_pickle = open(os.getcwd()+ "/" + "files" + "/author_dict.pickle",'wb')
Topic_dict_pickle = open(os.getcwd()+ "/" + "files" + "/topic_dict.pickle",'wb')
Title_file_dict_pickle = open(os.getcwd()+ "/" + "files" + "/title_file_dict.pickle",'wb')
File_topic_dict_pickle = open(os.getcwd()+ "/" + "files" + "/file_topic_dict.pickle",'wb')

intermediate_output_file.write("unextracted files:" + "/n")

# Unzipping the file
for file in os.listdir(filedir):
    if file.endswith(".tgz"):
        with tarfile.open(filedir+"/"+file, 'r') as t:
            try:
               t.extractall(unzipped_dir)
            except:
                intermediate_output_file.write(filedir+"/"+file + "/n")

intermediate_output_file.write("unflattened files:" + "/n")

# Flattening the unzipped directory structure so as to read individual files
for dirpath, dirnames, filenames in os.walk(unzipped_dir):
    for filename in filenames:
        try:
            os.rename(os.path.join(dirpath, filename), os.path.join(flattened_files_dir, filename))
            print(dirpath,dirnames,filename)
        except OSError:
            intermediate_output_file.write("Could not move %s " % os.path.join(dirpath, filename) + "/n")

# Topic Extraction and forming file - topic dictionary
File_topic_dict = {}
nlp = spacy.load('en')
documents = []
n = 3                                                                                                        # for taking top n tfidf scored keyword

for file in os.listdir(flattened_files_dir):
    read_xml_obj = Read_XML(flattened_files_dir+"/"+file)
    if read_xml_obj.parseable() == "parseable":
        documents.append(tb(read_xml_obj.getAbstract()))


def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

for file in os.listdir(flattened_files_dir):
    read_xml_obj = Read_XML(flattened_files_dir+"/"+file)
    topic = []
    if read_xml_obj.parseable() == "parseable":
        Title = read_xml_obj.getTitle()
        Title_spacy_doc = nlp(Title)
        for title_topic in Title_spacy_doc.noun_chunks:
            topic.append(title_topic.text)
        Abstract = read_xml_obj.getAbstract()
        Abstract_spacy_doc = nlp(Abstract)
        Abstract_blob = tb(Abstract)
        chunk_score_dict = {}
        for abstract_topic in Abstract_spacy_doc.noun_chunks:
            abstract_topic_blob = tb(abstract_topic.text)
            score = 0
            for word in abstract_topic_blob.words:
                score = score + tfidf(word, Abstract_blob, documents)
            chunk_score_dict[score] = abstract_topic.text
        ordered_tfidfscore_topic_dict = OrderedDict(list(chunk_score_dict.items()).sort(reverse = True))    # order the keywords wrt tfidf scores in descesding order
        j = 0
        while j < n:                                                                                        # append top n tfidf scored keywords to topic list
            topic.append(list(ordered_tfidfscore_topic_dict.items())[j][1])
            j = j+1
        File_topic_dict[file] = topic

# Forming dictionary and saving them in pickle format
Title_dict = {}
Author_dict = {}
Topic_dict = {}
Title_file_dict = {}

intermediate_output_file.write("unparseable files:" + "/n")

Title_value = 0
Author_value = 0
Topic_value = 0

for file in os.listdir(flattened_files_dir):
    read_xml_obj = Read_XML(flattened_files_dir+"/"+file)
    if read_xml_obj.parseable() == "parseable":
        Title = read_xml_obj.getTitle()
        Author_list = read_xml_obj.getAuthors()
        Topic_list = File_topic_dict[file]
        Title_dict[Title] = Title_dict.get(Title,str(Title_value)+"Ti")                                 # Title dictionary creation
        Title_value = Title_value+1
        for author in Author_list:
            Author_dict[author] = Author_dict.get(author,str(Author_value)+"Au")                        # Author dictionary creation
            Author_value = Author_value + 1
        for topic in Topic_list:
            Topic_dict[topic] = Topic_dict.get(topic,str(Topic_value)+"To")                             # Topic dictionary creation
            Topic_value = Topic_value + 1
        Title_file_dict[Title] = file
    else:
        intermediate_output_file.write(flattened_files_dir + "/" + file + "/n")

pickle.dump(Title_dict,Title_dict_pickle)
pickle.dump(Author_dict,Author_dict_pickle)
pickle.dump(Topic_dict,Topic_dict_pickle)
pickle.dump(Title_file_dict,Title_file_dict_pickle)
pickle.dump(File_topic_dict,File_topic_dict_pickle)

Title_dict_pickle.close()
Author_dict_pickle.close()
Topic_dict_pickle.close()
Title_file_dict_pickle.close()
File_topic_dict_pickle.close()

# Forming and Saving DBJSON
for file in os.listdir(flattened_files_dir):
    read_xml_obj = Read_XML(flattened_files_dir+"/"+file)
    if read_xml_obj.parseable() == "parseable":
        Title = read_xml_obj.getTitle()
        Author_list = read_xml_obj.getAuthors()
        Topic_list = File_topic_dict[file]
        Cit_Title_list = read_xml_obj.getCitationTitle()
        Title_id = Title_dict[Title]
        Author_list_id = [Author_dict[author] for author in Author_list]
        Topic_list_id = [Topic_dict[topic] for topic in Topic_list]
        Cit_Title_list_id = [Title_dict[cit_title] for cit_title in Cit_Title_list]
        Paper_obj = Paper(Title_id,Author_list_id,Topic_list_id,Cit_Title_list_id)




intermediate_output_file.close()