# Создание новых экземпляров объектов класса может быть отличным способом отслеживать значения с помощью атрибутов, связанных с объектом. Значения этих атрибутов можно легко изменить на уровне объекта. Следующий код иллюстрирует известную цитату Джорджа Бернарда Шоу, использующую объекты для представления людей. Заполните пробелы, чтобы код удовлетворял описанному в цитате поведению.


class Person:
    apples = 0
    ideas = 0


johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1


def exchange_apples(you, me):
    you.apples, me.apples = me.apples, you.apples
    return you.apples, me.apples


def exchange_ideas(you, me):
    you.ideas, me.ideas = you.ideas + me.ideas, you.ideas + me.ideas
    return you.ideas, me.ideas


exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(
    johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(
    johanna.ideas, martin.ideas))
