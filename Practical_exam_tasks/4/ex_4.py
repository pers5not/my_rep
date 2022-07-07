# 4.	Разработать класс очереди печати сотрудников. Предусмотреть в классе методы: помещение документа в очередь печати, извлечение следующего документа из очереди печати, проверка наличия документов в очереди. При помещении документа задается его приоритет, извлекаются в первую очередь документы с более высоким приоритетом.


import heapq
from enum import Enum


class Priority(Enum):
    HIGH = 1
    NORMAL = 2
    LOW = 3


class PrintQueue():

    def __init__(self, emloyes=[]) -> None:
        self.employes = emloyes

    def addEmployes(self, employe):
        heapq.heappush(self.employes, employe)

    def getEmployes(self):
        next_item = heapq.heappop(self.employes)
        return next_item

    def queueCheck(self):
        return len(self.employes)

    def __str__(self) -> str:
        return self.employes


# printqueue = PrintQueue()
# printqueue.addEmployes((Priority.LOW.value, "Alex", "1.txt"))
# printqueue.addEmployes((Priority.HIGH.value, "Ivan", "2.doc"))
# printqueue.addEmployes((Priority.NORMAL.value, "Oleg", "3.pdf",))
# printqueue.addEmployes((Priority.LOW.value, "Ignat", "4.xlsx",))
# printqueue.addEmployes((Priority.NORMAL.value, "Mihail", "5.json",))
# printqueue.addEmployes((Priority.HIGH.value, "Alina", "6.jpg",))

# for elem in printqueue.employes:
#     print(elem)

# for i in range(len(printqueue.employes)):
#     print(f" документов в очереди - {printqueue.queueCheck()}")
#     printqueue.getEmployes()
# print("Документов в очереди 0")
