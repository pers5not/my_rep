# 5. Створіть клас Студент, який містить перелік оцінок. Створіть клас Група, де знаходиться список студентів. Створіть спосіб виставлення оцінок студентів групи. Створити клас, який дозволяє зберігати та отримувати інформацію про студентів, які отримали певні оцінки (1, 2, 3, 4, 5).

from Students import Student
from Group import Group
from rate import rate
from StudentsByGrades import StudentsByGrades
from termcolor import colored, cprint


def c_print(ls):
    count = 0
    for k, v in ls.items():
        cprint(f"{k} -> оценка {v.name}",
               'magenta', attrs=['bold'])
        count += 1
    print(f"Всего - {count} человек")


def zap_list(ls):
    zap = open(
        f"qualifying_exam/Made/5/{input(f'Введите имя файла - ')}.txt", 'w')
    for k, v in ls.items():
        zap.write(f"{k} -> оценка {v}\n")


fhand = open(
    'qualifying_exam/Made/5/list_students.txt', 'r')

students_grades = Student
g = Group(fhand)
g.addListStudents()
r = rate(g.getStudentsList(), students_grades)
students_by_grades = StudentsByGrades(r)

students_by_grades.add_sort_students_grades()

a = students_by_grades.get_students_who_got_five()
b = students_by_grades.get_students_who_got_four()
c = students_by_grades.get_students_who_got_three()
d = students_by_grades.get_students_who_got_two()
e = students_by_grades.get_students_who_got_one()

print("Отличники")
zap_list(a)
print("Хорошисты")
zap_list(b)
print("Троешники")
zap_list(c)
print("Двоешники")
zap_list(d)
print("На отчисление")
zap_list(e)

c_print(a)
c_print(b)
c_print(c)
c_print(d)
c_print(e)

print(students_by_grades.students_who_got_five)
