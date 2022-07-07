try:
    hrs = float(input("Enter Hours:"))
    rrs = float(input("Enter Hours:"))
except:
    print("You entered an invalid value")
    quit()


def computepay(h, r):
    if h >= 40:
        return ((h - 40) * (1.5 * r)) + (40 * r)
    else:
        return h * r


p = computepay(hrs, rrs)
print("Pay", p)
