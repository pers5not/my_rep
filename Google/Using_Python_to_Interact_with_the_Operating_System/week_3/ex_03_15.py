# Мы работаем с файлом CSV, который содержит информацию о сотрудниках. Каждая запись имеет поле имени, за которым следует поле номера телефона и поле роли. Поле номера телефона содержит номера телефонов в США, и его необходимо преобразовать в международный формат, добавив «+1-» перед номером телефона. Заполните регулярное выражение, используя группы, чтобы использовать для этого функцию transform_record.

import re


def transform_record(record):
    new_record = re.sub(r',(?=\d)', ',+1-', record)
    return new_record


print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer
