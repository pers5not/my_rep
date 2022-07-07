# 8. Розробіть програму  для визначення найменшої цифри у введеному користувачем числі

import re


def zero_counter(num):
    smallest_num = None
    while True:
        if ',' in num or '.' in num or '-' in num or ' ' in num:
            num = re.sub(r'\-|\.|\,| ', '', num)
        if num.isdigit():
            for i in num:
                if smallest_num == None:
                    smallest_num = int(i)
                elif int(i) < smallest_num:
                    smallest_num = int(i)
            print(f"Найменша цифра в числі {num} - {smallest_num}")
            break
        else:
            print("Вы ввели не число попробуйте еще раз - ")
            num = input()


zero_counter(input("Введіть число - "))
print()
zero_counter("-123567556565189")
print()
zero_counter("888880777777.35555551")
print()
zero_counter("9888880,39992")
print()
zero_counter("-158792,29577771")
