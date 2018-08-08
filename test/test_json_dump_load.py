from poc1.main.classFiles import Paper
import json
import os

Paper_obj = Paper("1Ti",["1Au","2Au"],["1To","2To"],["2Ti","3Ti"])
#Paper_obj = Paper("1Ti","1Au","1To","2Ti")
b = u'{"authors": ["1Au", "2Au"], "topics": ["1To", "2To"], "title": "1Ti", "citpapers": ["2Ti", "3TI"]}'
obj = json.loads(b)
json_file = open(os.getcwd() + "/files/" + "json_test.json","w")


s = json.dumps(Paper_obj.__dict__)
json_file.write(s + "\n")
json_file.write(b + "\n")
json_file.close()
s_obj = json.loads(s)

#print(repr(obj))
print(Paper_obj.title)
print(s)
print(s_obj)
print(s_obj['authors'])