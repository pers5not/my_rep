# Заполните пробелы в функции nametag, чтобы она использовала метод формата для возврата first_name и первого инициала last_name, за которым следует точка. Например, nametag("Джейн", "Смит") должен возвращать "Джейн С."
def nametag(first_name, last_name):
    return("{} {}.".format(first_name, last_name[0]))


print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."
