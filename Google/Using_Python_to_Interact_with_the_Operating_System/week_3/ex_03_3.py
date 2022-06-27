import re

print(re.search(r'Py.*n', 'Pygmalion'))
print(re.search(r'Py.*n', 'Python programming'))
print(re.search(r'Py[a-z]*n', 'Python programming'))
print(re.search(r'Py[a-z]*n', 'Pyn'))
print(re.search(r'o+l+', 'goldfish'))
print(re.search(r'o+l+', 'woollly'))
print(re.search(r'p?each', 'To each their one'))
print(re.search(r'p?each', 'I like peaches'))
