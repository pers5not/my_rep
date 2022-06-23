# Давайте вернемся к нашей функции lucky_number. Мы хотим изменить его, чтобы вместо вывода сообщения оно возвращало сообщение. Таким образом, вызывающая линия может распечатать сообщение или сделать с ним что-то еще, если это необходимо. Заполните пробелы, чтобы завершить код, чтобы заставить его работать.

def lucky_number(name):
    number = len(name) * 9
    return "Hello " + name + ". Your lucky number is " + str(number)


print(lucky_number("Kay"))
print(lucky_number("Cameron"))
