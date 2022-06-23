# Давайте создадим функцию, которая превращает текст в поросячью латынь: простое преобразование текста, которое изменяет каждое слово, перемещая первый символ в конец и добавляя «ау» в конец. Например, python заканчивается как ythonpay.
from hashlib import new


def pig_latin(text):
    say = "ay"
    new_text = []
    words = text.split(' ')
    for word in words:
        new_word = word[0]
        word = word.replace(word[0], '') + new_word + say
        new_text.append(word)
    return ' '.join(new_text)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun"))
