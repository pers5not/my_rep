# Розробіть програму для визначення кількості голосних букв у рядку, що ввів користувач.
# У введеному {detect(my_text)} тексті {consonants} приголосних букв

from langdetect import detect


vovels_let = {'uk': 'аеиіоу',
              'ru': 'ауоыиэяюёе',
              'en': 'aeiou'}


def vowels(my_text):
    count = 0
    if detect(my_text) in vovels_let:
        for let in my_text:
            if let in vovels_let[detect(my_text)]:
                count += 1
            else:
                continue
    else:
        print("Вы ввели бред")
    print(f"У введеному {detect(my_text)} тексті {count} голосних букв")


vowels(input("Введіть текст - "))
vowels("Розробіть програму для визначення кількості голосних букв у рядку, що ввів користувач.")
vowels("Develop a program to determine the number of vowels in the line entered by the user.")
vowels("Разработайте приложение для определения количества гласных букв в строке, которую ввел пользователь.")
