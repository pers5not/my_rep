# Функция highlight_word изменяет заданное слово в предложении на его версию в верхнем регистре. Например, highlight_word("Хорошего дня", "хорошего") возвращает "Хорошего дня". Можете ли вы написать эту функцию всего в одну строку?

def highlight_word(sentence, word):
    return(sentence.replace(word, word.upper()))


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
