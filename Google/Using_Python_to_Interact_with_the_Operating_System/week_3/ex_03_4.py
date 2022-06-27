import re

print(re.search(r'.com', 'wellcome'))
print(re.search(r'\.com', 'well.come'))
print(re.search(r'\w*', 'This is excample'))
print(re.search(r'\w*', 'And_this_is_excample'))
