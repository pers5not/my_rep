# Розробіть програму  для визначення кількості нулів у введеному користувачем числі.
import re


def zero_counter(num):
    count = 0
    while True:
        if ',' in num or '.' in num or '-' in num or ' ' in num:
            num = re.sub(r'\-|\.|\,| ', '', num)
        if num.isdigit():
            for i in num:
                if int(i) == 0:
                    count += 1
                else:
                    continue
            print(f"{count} - нулів в числі {num}")
            break
        else:
            print("Вы ввели не число попробуйте еще раз - ")
            num = input()


print()
zero_counter(input("Введіть число - "))
print()
zero_counter("-123056789")
print()
zero_counter("103.301")
print()
zero_counter("023,300")
print()
zero_counter("-100002,2000001")
