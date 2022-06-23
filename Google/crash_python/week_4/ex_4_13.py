# Функция format_address разделяет части адресной строки на новые строки: house_number и street_name и возвращает: «дом номер X на улице Y». Формат входной строки: числовой номер дома, за которым следует название улицы, которое может содержать цифры, но не само по себе, и может состоять из нескольких слов. Например, «123 Main Street», «1001 1st Ave» или «55 North Center Drive». Заполните пробелы, чтобы завершить эту функцию.

def format_address(address_string):
    address_string = address_string.split(' ')
    number_h = 0
    streat = ''
    for num in address_string:
        if num.isdigit():
            number_h = int(num)
        else:
            streat += num
    return (f"house number {number_h} on street named {streat}")


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
