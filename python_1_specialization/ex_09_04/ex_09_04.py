name = input("Entaer file name: ")
if len(name) < 1:
    name = "mbox-short.txt"

handel = open(f"python_1_specialization/ex_09_04/{name}", "r")

counts = dict()
lst = list()

for line in handel:
    if line.startswith("From:"):
        mails = line.split()
        lst.append(mails[1])

for mail in lst:
    counts[mail] = counts.get(mail, 0) + 1

bigcount = None
bigmail = None

for mail, count in counts.items():
    if bigcount == None or count > bigcount:
        bigcount = count
        bigmail = mail
print(bigmail, bigcount)
