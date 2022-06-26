# Функция file_date создает новый файл в текущем рабочем каталоге, проверяет дату изменения файла и возвращает только дату временной метки в формате гггг-мм-дд. Заполните пробелы, чтобы создать файл с именем «newfile.txt», и проверьте дату его изменения.
import os
import datetime


def file_date(filename):
    # Create the file in the current directory
    file = open(filename, 'w')
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    time = datetime.datetime.fromtimestamp(timestamp)
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return ("{}".format(time.strftime("%Y-%m-%d")))


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd
