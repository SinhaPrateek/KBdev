import pandas as pd
import os,sys
from read_xml import Read_XML
import tarfile

filedir = os.getcwd()+ "/" + "files" + "/" + "archives/acl-arc-160301-parscit"
unzipped_dir = os.getcwd()+ "/" + "files" + "/" + "unzipped"
flattened_files_dir = os.getcwd()+ "/" + "files" + "/" + "flattened_unzipped"
intermediate_output_file = open(os.getcwd()+ "/" + "files" + "/intermediate_output.txt",'w')

intermediate_output_file.write("unextracted files:")

# Unzipping the file
for file in os.listdir(filedir):
    if file.endswith(".tgz"):
        with tarfile.open(filedir+"/"+file, 'r') as t:
            try:
               t.extractall(unzipped_dir)
            except:
                intermediate_output_file.write(filedir+"/"+file)

intermediate_output_file.write("unflattened files:")

# Flattening the unzipped directory structure so as read individual files
for dirpath, dirnames, filenames in os.walk(unzipped_dir):
    for filename in filenames:
        try:
            os.rename(os.path.join(dirpath, filename), os.path.join(flattened_files_dir, filename))
            print(dirpath,dirnames,filename)
        except OSError:
            intermediate_output_file.write("Could not move %s " % os.path.join(dirpath, filename))

# Forming dictionary
Title_dict = {}
Author_dict = {}
Abstract_dict = {}

for file in os.listdir(flattened_files_dir):
    read_xml_obj = Read_XML(file)
    Title = read_xml_obj.getTitle()



intermediate_output_file.close()