# Определите класс с именем Bike, который принимает строку и число с плавающей запятой в качестве входных данных и назначает эти входные данные соответственно двум переменным экземпляра, цвету и цене. Назначьте переменной testOne экземпляр Bike синего цвета и цену 89,99. Назначьте переменной testTwo экземпляр Bike фиолетового цвета и цены 25,0.
class Bike():
    def __init__(self, color, price) -> None:
        self.color = color
        self.price = price


tesOne = Bike("blue", 89.99)
testTwo = Bike('purple', 25.0)

print(f"Bike color {tesOne.color} price: {tesOne.price}")
print(f"Bike color {testTwo.color} price: {testTwo.price}")
