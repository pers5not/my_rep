score = input("Enter Score: ")

try:
    bal = float(score)
except:
    bal = -1
if bal > 1.0 or bal < 0:
    print("You entered an invalid value")
elif bal >= 0.9:
    print("A")
elif bal >= 0.8:
    print("B")
elif bal >= 0.7:
    print("C")
elif bal >= 0.6:
    print("D")
elif bal < 0.6:
    print("F")
