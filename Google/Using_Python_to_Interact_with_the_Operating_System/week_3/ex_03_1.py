import re
result = re.search(f"aza", "plaza")

print(result)

result = re.search(f"aza", "bazaar")

print(result)

print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "PANGAEA", re.IGNORECASE))
