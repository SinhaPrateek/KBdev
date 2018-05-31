import pickle
import os
from read_xml import Read_XML
import tarfile

filedir = os.getcwd()+ "/" + "files" + "/" + "archives/acl-arc-160301-parscit"
unzipped_dir = os.getcwd()+ "/" + "files" + "/" + "unzipped"
flattened_files_dir = os.getcwd()+ "/" + "files" + "/" + "flattened_unzipped"
intermediate_output_file = open(os.getcwd()+ "/" + "files" + "/intermediate_output.txt",'w')
Title_dict_pickle = open(os.getcwd()+ "/" + "files" + "/title_dict.pickle",'wb')
Author_dict_pickle = open(os.getcwd()+ "/" + "files" + "/author_dict.pickle",'wb')

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

# Flattening the unzipped directory structure so as read individual files
for dirpath, dirnames, filenames in os.walk(unzipped_dir):
    for filename in filenames:
        try:
            os.rename(os.path.join(dirpath, filename), os.path.join(flattened_files_dir, filename))
            print(dirpath,dirnames,filename)
        except OSError:
            intermediate_output_file.write("Could not move %s " % os.path.join(dirpath, filename) + "/n")

# Forming dictionary
Title_dict = {}
Author_dict = {}


intermediate_output_file.write("unparseable files:" + "/n")

Title_value = 0
Author_value = 0

for file in os.listdir(flattened_files_dir):
    read_xml_obj = Read_XML(file)
    if read_xml_obj.parseable() == "parseable":
        Title = read_xml_obj.getTitle()
        Author_list = read_xml_obj.getAuthors()
        Title_dict.get(Title,Title_value)
        Title_value = Title_value+1
        for author in Author_list:
            Author_dict.get(author,Author_value)
            Author_value = Author_value + 1

    else:
        intermediate_output_file.write(flattened_files_dir + "/" + file + "/n")

pickle.dump(Title_dict,Title_dict_pickle)
pickle.dump(Author_dict,Author_dict_pickle)

Title_dict_pickle.close()
Author_dict_pickle.close()

# Formong and Saving DBJSON


intermediate_output_file.close()