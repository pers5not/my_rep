# 2. Розробіть програму, що визначає чи є введений користувачем рядок паліндромом.

my_str = input("\nВведите свой текст - ")


def str_palindrom(my_str):
    if my_str.lower().replace(' ', '') == my_str[::-1].lower().replace(' ', ''):
        print(f"{my_str} == {my_str[::-1]}\nРядок є паліндромом\n")
    else:
        print(f"{my_str} != {my_str[::-1]}\nРядок не є паліндромом\n")


str_palindrom(my_str)
str_palindrom("123321")
str_palindrom("aba")
str_palindrom("abc")
str_palindrom("aibohphobia")
str_palindrom("Aibohphobia")
