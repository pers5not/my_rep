name = input("Enter file name: ")
if len(name) < 1:
    name = "python_1_specialization/ex_09_04/mbox-short.txt"

handle = open(f"{name}", "r")
counts = dict()

for line in handle:
    if line.startswith("From "):
        times = line.split()[5]
        hour = times.split(":")[0]
        counts[hour] = counts.get(hour, 0) + 1
lst = sorted([(k, v) for k, v in counts.items()])
for k, v in lst:
    print(k, v)
