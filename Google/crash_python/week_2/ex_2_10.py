# Функция Fractional_Part делит числитель на знаменатель и возвращает только дробную часть (число от 0 до 1). Завершите тело функции, чтобы она возвращала правильное число.
# Примечание. Поскольку деление на 0 приводит к ошибке, если знаменатель равен 0, функция должна возвращать 0 вместо попытки деления.
def fractional_part(numerator, denominator):

    if denominator != 0 and numerator / denominator > 0:
        return numerator / denominator % 1
    else:
        return 0


print(fractional_part(5, 5))  # Should be 0
print(fractional_part(5, 4))  # Should be 0.25
print(fractional_part(5, 3))  # Should be 0.66...
print(fractional_part(5, 2))  # Should be 0.5
print(fractional_part(5, 0))  # Should be 0
print(fractional_part(0, 5))  # Should be 0
