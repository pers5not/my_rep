fname = input("Enter file name: ")
fh = open(f"ex_08_05/{fname}", "r")
count = 0
for line in fh:
    if line.startswith("From:"):
        count += 1
        print(f"{line.strip().split()[1]}")
print(f"There were {count} lines in the file with From as the first word")
