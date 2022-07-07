# Определите класс с именем BankAccount, который принимает имя, которое вы хотите связать с вашим банковским счетом в строке, и целое число, представляющее сумму денег на счете. Конструктор должен инициализировать две переменные экземпляра из этих входных данных: name и amt. Добавьте строковый метод, чтобы при печати экземпляра BankAccount вы видели «Ваша учетная запись, [здесь идет имя], имеет [здесь идет start_amt] долларов». Создайте экземпляр этого класса с «Бобом» в качестве имени и 100 в качестве суммы. Сохраните это в переменную t1.

class BankAccount():
    def __init__(self, name, amt) -> None:
        self.name = name
        self.amt = amt

    def __str__(self) -> str:
        return f"Your account, {self.name}, has {self.amt} dollars."


t1 = BankAccount('Bob', 100)

print(t1)
