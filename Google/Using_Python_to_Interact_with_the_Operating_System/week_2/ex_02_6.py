# Функция parent_directory возвращает имя каталога, расположенного чуть выше текущего рабочего каталога. Помните, что «..» — это псевдоним относительного пути, который означает «перейти к родительскому каталогу». Заполните пробелы, чтобы завершить эту функцию.
import os


def parent_directory():

    # Create a relative path to the parent
    # of the current working directory
    relative_parent = os.path.join(os.getcwd(), os.pardir)
    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)


print(parent_directory())
