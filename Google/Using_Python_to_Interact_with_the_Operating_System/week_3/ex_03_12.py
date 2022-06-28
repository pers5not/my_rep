import re


print(re.search(r'[a-zA-Z]{5}', 'abc hello world a new'))
print(re.findall(r'[a-zA-Z]{5}', 'abc hello world a newline'))
print(re.findall(r'\b[a-zA-Z]{5}\b', 'abc hello world a newline'))
print(re.findall(r'\w{5,10}', 'I really like strawberries'))
print(re.findall(r'\w{5,}', 'I really like strawberries'))
print(re.findall(r's\w{,20}', 'I really like strawberries'))
