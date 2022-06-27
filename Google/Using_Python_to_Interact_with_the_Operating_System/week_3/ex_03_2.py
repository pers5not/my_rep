import re

print(re.search(r'[Pp]ython', 'Python'))
print(re.search(r'[a-z]way', 'The end of the highway'))
print(re.search(r'cloud[a-zA-Z0-9]', 'cloudy'))
print(re.search(r'cloud[a-zA-Z0-9]', 'cloud9'))
print(re.search(r'[^a-zA-Z0-9]', 'The end of the highway.'))
print(re.search(r'[^a-zA-Z0-9 ]', 'The end of the highway.'))
print(re.search(f'cat|dog', 'Hello my friend cat'))
print(re.search(f'cat|dog', 'Hello my dog friend'))
print(re.search(f'cat|dog', 'Hello my cat friend dog'))
print(re.findall(f'cat|dog', 'Hello my cat friend dog'))
