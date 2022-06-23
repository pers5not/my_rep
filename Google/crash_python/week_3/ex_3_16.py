# Функция even_numbers возвращает строку, разделенную пробелами, состоящую из всех положительных чисел, которые делятся на 2, вплоть до максимума, переданного в функцию, включительно. Например, even_numbers(6) возвращает «2 4 6». Заполните пробел, чтобы сделать эту работу.

def even_numbers(maximum):
    return_string = ""
    for x in range(1, maximum + 1):
        if x % 2 == 0:
            return_string += str(x) + " "
    return return_string.strip()


print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10))  # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed
