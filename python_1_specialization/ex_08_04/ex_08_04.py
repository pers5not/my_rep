fname = input("Enter file name: ")
fh = open(f"ex_08_04/{fname}", "r")
lst = list()
for line in fh:
    words = line.rstrip().split()
    for word in words:
        if word not in lst:
            lst.append(word)
print(sorted(lst))
