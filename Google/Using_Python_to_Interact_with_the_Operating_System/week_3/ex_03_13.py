import re
from unittest import result


log = 'July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade'

regex = r'\[(\d+)\]'
result = re.search(regex, log)
print(result[1])
result = re.search(regex, 'You need to start process number[65897555ss]')
print(result)


def extract_pit(log_line):
    regex = r'\[(\d+)\]'
    result = re.search(regex, log_line)
    if result is None:
        return ''
    return result[1]


f = open('log.txt')
cou = 0
for line in f:
    cou += 1
    print(extract_pit(line))
    print(line.strip())
print(cou)
f.close()

print(extract_pit(log))
print(extract_pit('You need to start process number[65897555ss]'))
