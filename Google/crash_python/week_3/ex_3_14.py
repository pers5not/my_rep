# Эта функция выводит таблицу умножения (где каждое число является результатом умножения первого числа в строке на число в верхней части столбца). Заполните пробелы, чтобы вызов multiplication_table(1, 3) распечатывал:
def multiplication_table(start, stop):
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            print(str(x*y), end=" ")
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above
