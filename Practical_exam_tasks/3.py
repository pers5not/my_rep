# 3. Розробіть програму, що змінює місцями сусідні слова у введеному реченні.


text = input("Введіть свій текст - ")


def swapWords(text):
    text = text.split(' ')
    for i in range(1, len(text), 2):
        text[i], text[i-1] = text[i-1], text[i]
    print(' '.join(text))


swapWords(text)
swapWords("Хороший програміст завжди дивиться і направо, і налево перш ніж перейти до вулиці з одностороннім рухом.")
swapWords("1, 2, 3, 4, 5, 6")
swapWords("7, 8, 9, 10, 11")
