# Функция convert_phone_number проверяет формат телефонного номера в США: XXX-XXX-XXXX (3 цифры, за которыми следует тире, еще 3 цифры, за которыми следует тире, и 4 цифры), и преобразует его в более формальный формат, который выглядит следующим образом: (ХХХ) ХХХ-ХХХХ. Заполните регулярное выражение, чтобы завершить эту функцию.
import re
# (?<!\S)(\d{3})-(\d{3})-(\d{4}\b)', r'(\1) \2-\3', phone)


def convert_phone_number(phone):
    result = re.sub(r'\b\s(\d{3})-', r' (\1) ', phone)
    return result


# My number is (212) 345-9999.
print(convert_phone_number("My number is 212-345-9999."))
# Please call (888) 555-1234
print(convert_phone_number("Please call 888-555-1234"))
print(convert_phone_number("123-123-12345"))  # 123-123-12345
# Phone number of Buckingham Palace is +44 303 123 7300
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))
