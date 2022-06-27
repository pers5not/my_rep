# Функция contains_acronym проверяет текст на наличие 2 или более символов или цифр, заключенных в круглые скобки, по крайней мере, первый символ в верхнем регистре (если это буква), возвращая True, если условие выполнено, или False в противном случае. Например, «Обмен мгновенными сообщениями (IM) — это набор коммуникационных технологий, используемых для обмена текстовыми сообщениями» должен возвращать значение True, поскольку (IM) удовлетворяет условиям соответствия». Заполните регулярное выражение в этой функции:
import re


def contains_acronym(text):
    pattern = r"\([A-Za-z0-9]*\)"
    result = re.search(pattern, text)
    return result != None


print(contains_acronym(
    "Instant messaging (IM) is a set of communication technologies used for text-based communication"))  # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication"))  # True
print(contains_acronym("Please do NOT enter without permission!"))  # False
print(contains_acronym(
    "PostScript is a fourth-generation programming language (4GL)"))  # True
print(contains_acronym(
    "Have fun using a self-contained underwater breathing apparatus (Scuba)!"))  # True
