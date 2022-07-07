class StudentsByGrades():
    students_who_got_five = {}
    students_who_got_four = {}
    students_who_got_three = {}
    students_who_got_two = {}
    students_who_got_one = {}

    def __init__(self, st_grade) -> None:
        self.st_grade = st_grade

    def add_sort_students_grades(self):
        for key, val in self.st_grade.items():
            if val == 5:
                StudentsByGrades.students_who_got_five[key] = val
            elif val == 4:
                StudentsByGrades.students_who_got_four[key] = val
            elif val == 3:
                StudentsByGrades.students_who_got_three[key] = val
            elif val == 2:
                StudentsByGrades.students_who_got_two[key] = val
            elif val == 1:
                StudentsByGrades.students_who_got_one[key] = val

    def get_students_who_got_five(self):
        return StudentsByGrades.students_who_got_five

    def get_students_who_got_four(self):
        return StudentsByGrades.students_who_got_four

    def get_students_who_got_three(self):
        return StudentsByGrades.students_who_got_three

    def get_students_who_got_two(self):
        return StudentsByGrades.students_who_got_two

    def get_students_who_got_one(self):
        return StudentsByGrades.students_who_got_one
