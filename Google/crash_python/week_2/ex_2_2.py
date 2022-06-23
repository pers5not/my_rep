# Эта функция сравнивает два числа и возвращает их в порядке возрастания.

# Заполните пробелы, чтобы оператор печати отображал результат вызова функции по порядку.

# Подсказка: если функция возвращает несколько значений, не забудьте сохранить эти значения в нескольких переменных.

def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1


smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)
