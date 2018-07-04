from main.classFiles import Paper
import os
import json

final_paper_class_file = os.getcwd()+ "/" + "files" + "/db_creation" + "/final_paper_class.json"

# read the paper class json file and save each paper class json to a list
with open(final_paper_class_file) as f:
    paper_class_json_list_unstripped = f.readlines()

paper_class_json_list = [x.strip() for x in paper_class_json_list_unstripped]


for paper_class_json in paper_class_json_list:
    paper_class_json_obj = json.loads(paper_class_json)
    Paper_obj = Paper(paper_class_json_obj['title'],paper_class_json_obj['authors'],paper_class_json_obj['topics'],paper_class_json_obj['citpapers'])
