fname = input("Enter file name: ")
fh = open(fname, 'r')

for line in fh:
    print(line.upper().rstrip())
