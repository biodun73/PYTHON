import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
j = json.loads(x)
print(j["name"])