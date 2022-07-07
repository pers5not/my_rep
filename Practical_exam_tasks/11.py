# Розробіть програму для визначення кількості голосних букв у рядку, що ввів користувач.
# У введеному {detect(my_text)} тексті {consonants} приголосних букв

from langdetect import detect

vowels_ua = 'аеиіоу'
vowels_ru = 'ауоыиэяюёе'
vowels_en = 'aeiou'


def vowels(my_text):
    count = 0
    consonants = 0
    for let in range(len(my_text)):
        if my_text[let] in vowels_ua or my_text[let] in vowels_ru or my_text[let] in vowels_en:
            count += 1
        else:
            consonants += 1
    print(f"У введеному {detect(my_text)} тексті {count} голосних букв")


vowels(input("Введіть текст - "))
vowels("Розробіть програму для визначення кількості голосних букв у рядку, що ввів користувач.")
vowels("Develop a program to determine the number of vowels in the line entered by the user.")
vowels("Разработайте приложение для определения количества гласных букв в строке, которую ввел пользователь.")
