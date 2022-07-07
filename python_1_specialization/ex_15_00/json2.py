import json

data = """[
{"id" : "001",
"x" : "2",
"name" : "Alex"
}, 
{ "id" : "003",
"x" : "3",
"name" : "Mihail"
}
]"""

info = json.loads(data)
print('User count', len(info))
for item in info:
    print('Name:', item["name"])
    print('Id:', item["id"])
    print('x:', item["x"])
