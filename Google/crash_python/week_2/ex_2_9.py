# Функция longest_word используется для сравнения 3 слов. Он должен вернуть слово с наибольшим количеством символов (и первым в списке, если они имеют одинаковую длину). Заполните пробел, чтобы это произошло.

def longest_word(word1, word2, word3):
    if len(word1) >= len(word2) and len(word1) >= len(word3):
        word = word1
    elif len(word2) >= len(word1) and len(word2) >= len(word3):
        word = word2
    else:
        word = word3
    return(word)


print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))
