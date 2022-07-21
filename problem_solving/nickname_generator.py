#!/usr/bin/env python3'
import random

user_name = input("Введите ваше имя - ").lower()
DICT_TRANSLIT = user_name.maketrans({"а": "a",
                                     "б": "b",
                                     "в": "v",
                                     "г": "g",
                                     "д": "d",
                                     "е": "e",
                                     "ж": "zh",
                                     "з": "z",
                                     "и": "i",
                                     "й": "j",
                                     "к": "k",
                                     "л": "l",
                                     "м": "m",
                                     "н": "n",
                                     "о": "o",
                                     "п": "p",
                                     "р": "r",
                                     "с": "s",
                                     "т": "t",
                                     "у": "u",
                                     "ф": "f",
                                     "х": "h",
                                     "ц": "c",
                                     "ч": "ch",
                                     "ш": "sh",
                                     "щ": "sh",
                                     "ъ": "'",
                                     "ы": "y",
                                     "ь": "'",
                                     "э": "'e",
                                     "ю": "yu",
                                     "я": "ya", })


f = open('funy_words.txt', 'r')
funy_words = [word.strip() for word in f]
email_symbols = ".-_"
email_domen = ['@gmail.com', "@mail.ru", "@yandex.ru", "@rambler.ru"]


def str_catenation(user_name):
    random_number = random.randint(1920, 2022)
    random_name = user_name.translate(
        DICT_TRANSLIT) + random.choice(email_symbols) + \
        random.choice(funy_words) + str(random_number) + \
        random.choice(email_domen)
    return random_name


def gen_email(user_name):
    if len(user_name) > 4:
        return str_catenation(user_name[:4])
    if user_name == '':
        return str_catenation(random.choice(funy_words)[:4])
    else:
        return str_catenation(user_name)

print(gen_email(user_name))