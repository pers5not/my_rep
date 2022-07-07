hrs = input("Enter Hours:")
rrs = input("Enter Hours:")
if float(hrs) >= 40:
    rrrs = (float(hrs) - 40) * (float(rrs) * 1.5)
    print((40 * float(rrs)) + rrrs)
else:
    print(float(hrs) * float(rrs))
