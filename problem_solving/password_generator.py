import random

user_name = input('Введите ваш логин - ')


def clean_user_choice(user_list):
    user_choice = []
    for choice in user_list:
        choice = int(choice)
        if choice not in user_choice and choice > 0 and choice <= 5:
            user_choice.append(int(choice))
        else:
            continue
    return user_choice


def add_symbol(list_sumbol):
    user_symbol_list = ''
    if 1 in list_sumbol:
        user_symbol_list += "abcdefghijklmnopqrstuvwxyz"
    if 2 in list_sumbol:
        user_symbol_list += "abcdefghijklmnopqrstuvwxyz".upper()
    if 3 in list_sumbol:
        user_symbol_list += "0123456789"
    if 4 in list_sumbol:
        user_symbol_list += "!#$%&()*+,-./:;<=>?@[\]^_`{|}~ "
    if 5 in list_sumbol:
        user_symbol_list = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[\]^_`{|}~ "
    return user_symbol_list


def generator_pas(add_symbol, pass_len):
    pas = ''
    for i in range(pass_len):
        pas += random.choice(add_symbol)
    return pas


while True:
    answer_user = input(
        f"{user_name} Вы хотите сгенерировать пароль? (y/n)").lower()
    if answer_user == "yes" or answer_user == "y":
        pass_len = int(input(f"Введите длину пароля - "))
        user_choice = input("""
Какие символы должен содержать Ваш пароль?
        
1 - буквы | "abcdefghijklmnopqrstuvwxyz"
2 - БОЛЬШИЕ БУКВЫ | "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
3 - цифры | "0123456789"
4 - специальные симолы | "!#$%&()*+,-./:;<=>?@[\]^_`{|}~ "
5 - все символы
exit - выйти из программы

Введите свой выбор через пробел 1 2 3 ........ 
---> """).split()
        if 'exit' in user_choice:
            print(f"{user_name} Вы завершили программу")
            break
        password = add_symbol(clean_user_choice(user_choice))
        if password:
            print(
                f"\n{user_name} Ваш пароль из {pass_len} символов: {generator_pas(password, pass_len)}")
            break
        else:
            print(f"\n{user_name} Вы ввели что-то не то {user_choice} сделйте правильный выбор 1 2 3......\n")
    elif answer_user == 'no' or answer_user == 'n' or answer_user == 'not':
        print(f"\n{user_name} Вы завершили программу")
        break
    else:
        print(f"\n{user_name} Ваш выбор {answer_user} а должно быть Y или N")
