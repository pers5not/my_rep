# Создайте класс с именем Animal, который принимает два числа в качестве входных данных и присваивает их соответственно двум переменным экземпляра: arms и legs. Создайте метод экземпляра, limbsкоторый при вызове возвращает общее количество конечностей животного. Назначьте переменной name spiderэкземпляр Animalс 4 руками и 4 ногами. Вызовите метод конечностей для spiderэкземпляра и сохраните результат в переменной name spidlimbs.

class Animal():
    def __init__(self, arms, legs) -> None:
        self.arms = arms
        self.legs = legs

    def limbs(self):
        return self.arms + self.legs


spider = Animal(4, 4)
spidlimbs = spider.limbs()

print(spidlimbs)
