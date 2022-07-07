fname = input("Enter file name: ")
fh = open(f"ex_07_02/{fname}", "r")
count = 0
result = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        pos_line = line.find(":")
        num_line = float(line[pos_line+1:].strip())
        count += 1
        result = result + num_line
print(f"Average spam confidence: {result / count}")
