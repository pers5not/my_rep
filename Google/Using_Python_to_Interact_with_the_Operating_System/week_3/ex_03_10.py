# Введите код, чтобы проверить, содержит ли переданный текст возможный почтовый индекс США, отформатированный следующим образом: ровно 5 цифр, а иногда, но не всегда, за которым следует тире с еще 4 цифрами. Перед почтовым индексом должен быть хотя бы один пробел, и он не может быть в начале текста.
import re


def check_zip_code(text):
    result = re.search(r"\s\d{5}|\s\d{5}-\d{4}", text)
    return result != None


print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code(
    "The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False
