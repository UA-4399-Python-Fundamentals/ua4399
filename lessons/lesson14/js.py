import json


x = '{ "name":"Liubov", "age":25, "city":"Lviv"}' 

d = json.loads(x)
print(d)
print(d.get("age"))
from pprint import pprint
with open("lessons\lesson14\data.json") as f:
    data = json.load(f)
pprint(data)


with open("lessons\lesson14\out.json", "w") as f:
    data = {
        "key": 152,
        "user":{
            "name": "Anna"
        }
    }
    print(data)
    json.dump(data, f)