CURRENT_YEAR = 2022


class Person():
    def __init__(self, name, year_born) -> None:
        self.name = name
        self.year_born = year_born

    def getAge(self):
        return CURRENT_YEAR - self.year_born

    def __str__(self) -> str:
        return f"{self.name} ({self.getAge()})"


class Student(Person):
    def __init__(self, name, year_born) -> None:
        Person.__init__(self, name, year_born)

        self.knowledge = 0

    def study(self):
        self.knowledge += 1


allice = Student('Alice Smith', 1990)
print(allice)
allice.study()
print(allice.knowledge)
