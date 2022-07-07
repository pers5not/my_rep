# Создайте класс AppleBasket, конструктор которого принимает два входных параметра: строку, представляющую цвет, и число, представляющее количество яблок. Конструктор должен инициализировать две переменные экземпляра: apple_color и apple_quantity. Напишите метод класса с именемувеличить, который увеличивает количество на 1 каждый раз, когда он вызывается. Вы также должны написать метод __str__ для этого класса, который возвращает строку формата: «Корзина с [количество здесь] [здесь идет цвет] яблок». например «Корзина из 4 красных яблок». или «Корзина из 50 синих яблок». (Написание тестового кода, который создает экземпляры и присваивает значения переменным, может помочь вам решить эту проблему!)

from importlib.util import set_loader


class AppleBasket():
    basket_count = 0

    def __init__(self, apple_color, apple_quantity) -> None:
        self.color = apple_color
        self.quantity = apple_quantity

    def increase(self):
        self.quantity += 1
        return self.quantity

    def __str__(self) -> str:
        return f"A basket of {self.quantity} {self.color} apples."


ap1 = AppleBasket('green', 7)

print(ap1)
ap1.increase()
print(ap1)
