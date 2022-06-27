# Мы работаем со списком цветов и некоторой информацией о каждом из них. Функция create_file записывает эту информацию в CSV-файл. Функцияcontents_of_file считывает этот файл в записи и возвращает информацию в хорошо отформатированном блоке. Заполните пробелы в функции contents_of_file, чтобы преобразовать данные в CSV-файле в словарь с помощью DictReader.

import os
import csv

# Create a file with data in it


def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row


def contents_of_file(filename):
    return_string = ""
    create_file(filename)
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            return_string += "a {} {} is {}\n".format(
                row["color"], row["name"], row["type"])
        return return_string


# Call the function
print(contents_of_file("flowers.csv"))
