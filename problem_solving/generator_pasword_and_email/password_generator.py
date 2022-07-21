#@sadlarry_kh ----> Александр
import random
import email_generator as email_gen

user_name = email_gen.user_name


def clean_user_choice(user_list):
    user_choice = []
    for choice in user_list:
        if choice.isdigit():
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
    for i in range(int(pass_len)):
        pas += random.choice(add_symbol)
    return pas


def get_password():
    choice_list = ['1', '2', '3', '4', 'exit']
    user_choice = ''
    while True:
        pass_len = input(f"Введите длину пароля - ")
        if pass_len.isdigit():
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
                return f"{user_name} Вы завершили программу"

            password = add_symbol(clean_user_choice(user_choice))

            if password:
                return generator_pas(password, pass_len)

            if user_choice not in choice_list:
                print("\n{} Вы сделали не правильный ввод ---> {} ПОВТОРИТЕ ПОПЫТКУ\n"
                      .format(user_name, user_choice))

        else:
            print("\n{} Вы ввели \"{}\" не число  ВВЕДИТЕ ЧИСЛО\n"
                  .format(user_name, pass_len.upper()))


def get_email():
    return email_gen.gen_email(user_name)


def get_password_and_email():
    return print("\n{2} ПОЛУЧИТЕ РАСПЕШИТЕСЬ \n\tВаш email: {1}\n\tВаш пароль: {0} ".\
        format(get_password(), get_email(), user_name))


while True:
    answer_user = input(
        f"""{user_name} Сделайте свой выбор? 
1 - сгенерировать пароль
2 - сгенировать e-mail
3 - сгенерировать и e-mail и пароль
exit - Выход 
---> """).lower()
    if answer_user == "1":
        print(f"{user_name} Ваш пароль: {get_password()}")
        break
    if answer_user == "2":
        print(f"\n{user_name}Ваш e-mail: {get_email()}")
        break
    if answer_user == "3":
        get_password_and_email()
        break
    if answer_user == "exit":
        print(f"{user_name} Вы вышли из программы")
        break
    else:
        print(
            f"\n{user_name} вы ввели \"{answer_user.upper()}\" НЕПРАВИЛЬНЫЙ ВВОД\n")
