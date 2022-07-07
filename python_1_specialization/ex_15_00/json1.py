import json

data = """
{
    "name" : "Alex",
    "phone" : {
        "type" : "intl",
        "number" : "+38 095 3767 993"
    },
    "email" : {
        "hide" : "yes"
    }
} """

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
