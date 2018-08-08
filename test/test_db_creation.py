#from poc1.main.classFiles import Paper
#from __future__ import absolute_import
#from .. import main.read_xml

from poc1.main.read_xml import Read_XML
import json
import os
from fuzzywuzzy import fuzz

flattened_files_dir = os.getcwd()+ "/" + "files" + "/" + "flattened_unzipped"
output_file = open(os.getcwd()+ "/" + "files" + "/db_creation" + "/test_db_creation.txt",'w')

Title_dict = {}
Author_dict = {}

Title_value = 0
Author_value = 0

for file in os.listdir(flattened_files_dir):
    read_xml_obj = Read_XML(flattened_files_dir+"/"+file)
    if read_xml_obj.parseable() == "parseable":
        output_file.write(file + "\n")
        Title = read_xml_obj.getTitle()
        Author_list = read_xml_obj.getAuthors()
        Cit_Title_list = read_xml_obj.getCitationTitle()

        if not any(key == Title for key in Title_dict.keys()):
            Title_dict[Title] = Title_dict.get(Title, str(Title_value) + "Ti")  # Title dictionary creation
        else:
            output_file.write("Repeated Main Title" + ":" + Title+ "\n")
        Title_value = Title_value + 1
        output_file.write(Title + ":::" + Title_dict[Title] + "\n")
        output_file.write("\n")
        for cit_title in Cit_Title_list:
            if cit_title != "" and (not any(key == cit_title for key in Title_dict.keys())):
                Title_dict[cit_title] = Title_dict.get(cit_title,str(Title_value) + "Ti")  # Adding citation title to title dict
            else:
                output_file.write("Repeated Citation Title"+ ":"+cit_title + "\n")
            Title_value = Title_value + 1
        for author in Author_list:
            for key in Author_dict.keys():                                                                  # Testing fuzzywuzzy
                if fuzz.token_set_ratio(key,author)>90:
                    output_file.write("Repeated Authors"+ ":"+ author + "===" + key + "(" + str(fuzz.token_set_ratio(key,author)) + ")" + "\n")

            if not any(key == author for key in Author_dict.keys()):
                Author_dict[author] = Author_dict.get(author,str(Author_value)+"Au")                        # Author dictionary creation
            Author_value = Author_value + 1



        output_file.write("\n")
        output_file.write("AUTHOR ::: AUTHOR ID IN AUTHOR DICT" + "\n")
        output_file.write("\n")
        for author in Author_list:
            output_file.write(str(author) + ":::" + Author_dict[author] + "\n")
        output_file.write("\n")
        output_file.write("CITATION TITLE ::: CITATION ID IN TITLE DICT" + "\n")
        output_file.write("\n")
        for cit_title in Cit_Title_list:
            if cit_title != "":
               output_file.write(str(cit_title) + ":::" + Title_dict[cit_title] + "\n")
        output_file.write("\n")
        output_file.write("---------------------" + "\n")
        output_file.write("\n")
