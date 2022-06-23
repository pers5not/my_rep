# Следующий код может привести к бесконечному циклу. Исправьте код, чтобы он успешно завершился для всех номеров.

# Примечание. Попробуйте запустить функцию с числом 0 в качестве входных данных и посмотрите, что получится!

def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0:
        if n <= 0:
            return False
        else:
            n = n / 2
            return True
    if n == 1:
        return True

    return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False
