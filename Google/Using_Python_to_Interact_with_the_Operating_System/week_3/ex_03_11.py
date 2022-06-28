import re

result = re.search(r'^(\w*), (\w*)$', 'Lovelace, Ada')
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
print(f"{result[2]} {result[1]}")


def rearange_name(name):
    result = re.search(r'^([\w \.-]*), ([\w \.-]*)$', name)
    if result is None:
        return name
    return(f"{result[2]} {result[1]}")


print(rearange_name('Lovelace, Ada'))
print(rearange_name('Stivenson, Radgi'))
print(rearange_name('Canady, John F.'))
print(rearange_name('Canady, John Felix'))
