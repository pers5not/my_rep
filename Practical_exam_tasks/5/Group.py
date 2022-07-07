class Group():
    def __init__(self, open_file,) -> None:
        self.name_students = []
        self.open_file = open_file

    def addListStudents(self):
        for student in self.open_file:
            self.name_students.append(student.replace('\n', ''))

    def getStudentsList(self):
        return self.name_students


fhand = open(
    'qualifying_exam/Made/5/list_students.txt', 'r')

g = Group(fhand)
g.addListStudents()
print(g.getStudentsList())
