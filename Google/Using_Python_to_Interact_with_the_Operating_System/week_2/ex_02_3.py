# Функция create_python_script создает новый скрипт python в текущем рабочем каталоге, добавляет к нему строку комментариев, объявленную переменной 'comments', и возвращает размер нового файла. Заполните пробелы, чтобы создать сценарий с именем «program.py».
import os


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, 'w') as file:
        file.write(comments)
    filesize = os.path.getsize(filename)
    return(filesize)


print(create_python_script("week_2/program.py"))
