# Функция check_time проверяет формат времени 12-часового формата следующим образом: час находится в диапазоне от 1 до 12 без ведущего нуля, за которым следует двоеточие, затем минуты от 00 до 59, затем необязательный пробел, а затем AM или PM, в верхнем или нижнем регистре. Для этого заполните регулярное выражение. Сколько понятий, которые вы только что узнали, вы можете здесь использовать?

import re


def check_time(text):
    pattern = r"\d{1,2}:[0-5][0-9]\s?[AapPMm]"
    result = re.search(pattern, text)
    return result != None


print(check_time("12:45pm"))  # True
print(check_time("9:59 AM"))  # True
print(check_time("6:60am"))  # False
print(check_time("five o'clock"))  # False
