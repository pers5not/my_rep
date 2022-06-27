# Функция check_web_address проверяет, соответствует ли переданный текст веб-адресу верхнего уровня, т. е. содержит ли он буквенно-цифровые символы (включая буквы, цифры и символы подчеркивания), а также точки, тире и знак плюс, за которыми следует точка. и символьный домен верхнего уровня, такой как «.com», «.info», «.edu» и т. д. Для этого заполните регулярное выражение, используя escape-символы, подстановочные знаки, квалификаторы повторения, начало и конец- внестрочные символы и классы символов.
import re


def check_web_address(text):
    pattern = r"^\w.*\.[a-zA-Z]*$"
    result = re.search(pattern, text)
    return result != None


print(check_web_address("gmail.com"))  # True
print(check_web_address("www@google"))  # False
print(check_web_address("www.Coursera.org"))  # True
print(check_web_address("web-address.com/homepage"))  # False
print(check_web_address("My_Favorite-Blog.US"))  # True
