# Создайте класс с именем Cereal, который принимает три входных данных: 2 строки и 1 целое число, и присваивает их трем переменным экземпляра в конструкторе: name, brandи fiber. Когда экземпляр Cerealраспечатывается, пользователь должен увидеть следующее: «[имя] хлопья производятся [брендом] и содержат [целое число волокон] граммов клетчатки в каждой порции!» Для имени переменной c1назначьте экземпляр Cerealимени , бренда и волокна . Для имени переменной назначьте экземпляр имени , бренда и волокна . Практика печати обоих!"Corn Flakes""Kellogg's"2c2Cereal"Honey Nut Cheerios""General Mills"3

class Cereal:
    def __init__(self, name, brand, fiber) -> None:
        self.name = name
        self.brand = brand
        self.fiber = fiber

    def __str__(self) -> str:
        return f"{self.name} cereal is produced by {self.brand} and has {self.fiber} grams of fiber in every serving!"


c1 = Cereal("Corn Flakes", "Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios", "General Mills", 3)

print(f"{c1}\n{c2}")
