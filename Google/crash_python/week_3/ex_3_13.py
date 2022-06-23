# Завершите функцию digits(n), которая возвращает количество цифр в числе. Например: 25 имеет 2 цифры, а 144 — 3 цифры. Совет: вы можете определить цифры числа, разделив его на 10 один раз на цифру, пока не останется цифр.
def digits(n):
    count = 0
    if n == 0:
        return 1
    while (n != 0):
        n = n // 10
        count += 1
    return count


print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))    # Should print 1
