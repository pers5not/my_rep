# Розробіть програму для визначення яких саме цифр у введеному користувачем числі більше, парних чи непарних.
import re


def even_odd_numbers(num):
    paired_count = 0
    unpaired_count = 0
    while True:
        if ',' in num or '.' in num or '-' in num or ' ' in num:
            num = re.sub(r'\-|\.|\,| ', '', num)
        if num.isdigit():
            for i in num:
                if int(i) % 2 == 0:
                    paired_count += 1
                else:
                    unpaired_count += 1
            print(
                f"{paired_count} - парних цифр\n{unpaired_count} - непарних цифр")
            if unpaired_count > paired_count:
                print(f"в числі {num} непарних цифр більше")
            elif paired_count > unpaired_count:
                print(f"в числі {num} парних цифр більше")
            else:
                print(f"в числі {num} парних і непарних цифр однаково")
            break
        else:
            print("Вы ввели не число попробуйте еще раз - ")
            num = input()


print()
even_odd_numbers(input("Введіть число - "))
print()
even_odd_numbers("-123456789")
print()
even_odd_numbers("123.321")
print()
even_odd_numbers("123,321")
print()
even_odd_numbers("-12,21")
print()
even_odd_numbers("000000")
