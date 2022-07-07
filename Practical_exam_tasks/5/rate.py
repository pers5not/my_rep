from termcolor import colored, cprint


def rate(name_students, s_grades):
    student_rate = {}
    print("""
        Перечень оценок:
A - 5
B - 4
C - 3
D - 2
E - 1
q - ВЫХОД
        """)
    i = 0
    while i < len(name_students):
        st_grade = input(f"{name_students[i]} Введите Вашу оценку - ")
        if st_grade.isdigit() and int(st_grade) <= 5 and int(st_grade) >= 1:
            st_grade = int(st_grade)
            if st_grade == s_grades.A.value:
                student_rate[name_students[i]] = s_grades.A
                i += 1
            elif st_grade == s_grades.B.value:
                student_rate[name_students[i]] = s_grades.B
                i += 1
            elif st_grade == s_grades.C.value:
                student_rate[name_students[i]] = s_grades.C
                i += 1
            elif st_grade == s_grades.D.value:
                student_rate[name_students[i]] = s_grades.D
                i += 1
            elif st_grade == s_grades.E.value:
                student_rate[name_students[i]] = s_grades.E
                i += 1
        elif st_grade == 'q':
            print(colored("ВЫ ЗАКРЫЛИ ПРОГРАММУ", 'red',
                          attrs=['reverse', 'blink', 'bold']))
            break
        else:
            print(colored("ОЦЕНКА НЕ ВЫСТАВЛЕНА ВЫ ВВЕЛИ НЕ ВЕРНОЕ ЗНАЧЕНИЕ",
                          'red', attrs=['reverse', 'blink', 'bold']))
    return student_rate
