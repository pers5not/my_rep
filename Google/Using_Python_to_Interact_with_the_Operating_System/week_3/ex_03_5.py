from ast import pattern
import re


print(re.search(r'A.*a', 'Argentina'))
print(re.search(r'A.*a', 'Azeibarjan'))
print(re.search(r'^A.*a$', 'Azeibarjan'))
print(re.search(r'^A.*a$', 'Australia'))


pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

print(re.search(pattern, "_this_is_valid_variable_name"))
print(re.search(pattern, "this isn't variable_name"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "my_variable_1"))
print(re.search(pattern, "1_my_variable"))
