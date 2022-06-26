# Функция new_directory создает новый каталог внутри текущего рабочего каталога, затем создает новый пустой файл внутри нового каталога и возвращает список файлов в этом каталоге. Заполните пробелы, чтобы создать файл «script.py» в каталоге «PythonPrograms».
import os


def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)
    # Create the new file inside of the new directory
    os.chdir(directory)
    with open(filename, 'w') as file:
        pass
    os.chdir("..")
    os.chdir("..")
    # Return the list of files in the new directory
    return os.listdir(directory)


print(new_directory("week_2/PythonPrograms", "script.py"))
