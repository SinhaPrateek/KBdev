from main.classFiles import Paper
import json

Paper_obj = Paper("1Ti",["1Au","2Au"],["1To","2To"],["2Ti","3Ti"])
#Paper_obj = Paper("1Ti","1Au","1To","2Ti")
b = u'{"authors": ["1Au", "2Au"], "topics": ["1To", "2To"], "title": "1Ti", "citpapers": ["2Ti", "3TI"]}'
obj = json.loads(b)

s = json.dumps(Paper_obj.__dict__)

print(repr(obj))
print(Paper_obj.title)
print(s)