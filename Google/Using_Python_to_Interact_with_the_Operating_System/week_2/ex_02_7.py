import csv

f = open('my_blade.txt')

my_csv = csv.reader(f)

for row in my_csv:
    id_w, last_name, first_name, patronymic, num, speciality = row
    print('ID: {} Last_name: {} First_name {}: Patronymic {} Num {} Speciality {}'.format(id_w,
          last_name, first_name, patronymic, num, speciality))
