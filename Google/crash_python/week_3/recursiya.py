def fac(n):
    if n < 2:
        return 1
    print(n * fac(n - 1))
    return n * fac(n - 1)


fac(5)
