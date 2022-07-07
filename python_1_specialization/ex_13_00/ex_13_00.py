import urllib.request
import urllib.parse
import urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()

for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = sorted([(k, v) for v, k in counts.items()])
for k, v in lst:
    print(f"{v} ----- {k}")
