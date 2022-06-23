# Учитывая список имен файлов, мы хотим переименовать все файлы с расширением hpp в расширение h. Для этого мы хотели бы сгенерировать новый список с именем newfilenames, состоящий из новых имен файлов. Заполните пробелы в коде, используя любой из методов, которые вы уже изучили, например, цикл for или понимание списка.
filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []

for i in filenames:
    if '.hpp' in i:
        newfilenames.append(i.replace('hpp', '.h'))
    else:
        newfilenames.append(i)

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
