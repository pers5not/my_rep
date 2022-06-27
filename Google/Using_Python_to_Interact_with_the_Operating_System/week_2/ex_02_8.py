import csv


my_list = [['Абиев Марик Олегович', 'БПИ211'],
           ['Абулханов Дамир Зуфарович', 'БПИ212']]
with open('hosts.csv', 'w') as hosts:
    writer = csv.writer(hosts)
    writer.writerows(my_list)
