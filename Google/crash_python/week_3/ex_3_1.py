# Заполните пробелы, чтобы функция print_prime_factors напечатала все простые множители числа. Простой множитель — это число, которое является простым и делит другое без остатка.

def print_prime_factors(number):
    factor = 2
    while factor <= number:
        if number % factor == 0:
            # If it is, print it and divide the original number
            print(factor)
            number = number / factor
        else:
            factor += 1
    return "Done"


print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT
