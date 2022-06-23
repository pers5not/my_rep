# Код ниже определяет класс *Elevator*. У лифта есть текущий этаж, а также верхний и нижний этажи, которые являются минимальным и максимальным этажами, на которые он может подняться. Заполните пробелы, чтобы лифт прошел через запрошенные этажи.
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current

    def up(self):
        if self.current >= -1 and self.current <= 9:
            self.current += 1
            return self.current

    def down(self):
        if self.current >= 0 and self.current <= 10:
            self.current -= 1
            return self.current

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if self.current >= -1 and self.current <= 9:
            self.current = floor
            return self.current

    def __str__(self) -> str:
        return f"Current floor: {self.current}"


elevator = Elevator(-1, 10, 0)

# Этот класс довольно пустой и мало что делает. Чтобы проверить, правильно ли работает ваш класс *Elevator*, запустите приведенные ниже блоки кода.
# elevator.up()
# elevator.current  # should output 1
# elevator.down()
# elevator.current  # should output 0
# elevator.go_to(10)
# elevator.current  # should output 10

# Если вы получили сообщение NameError, обязательно сначала запустите блок кода определения класса Elevator. Если вы получаете сообщение AttributeError, обязательно инициализируйте self.current в своем классе Elevator.

# Как только вы заставите вышеуказанные методы выводить 1, 0 и 10, вы успешно написали код класса Elevator и его методов. Отличная работа!

# Для методов «вверх» и «вниз» учитывали ли вы верхний и нижний этажи? Имейте в виду, что лифт не должен подниматься выше верхнего этажа или ниже нижнего этажа. Чтобы проверить это, попробуйте приведенный ниже код и убедитесь, что он работает должным образом. Если это не так, то вернитесь и измените методы, чтобы этот код вел себя правильно.

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)

elevator.up()
elevator.down()
print(elevator.current)  # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()

print(elevator.current)  # should be 1

# Теперь добавьте метод str к вашему определению класса Elevator выше, чтобы при печати лифта с помощью метода print() мы получали текущий этаж вместе с сообщением. Например, на 5-м этаже должно быть написано «Текущий этаж: 5».

elevator.go_to(5)
print(elevator)

# Помните, Python использует метод по умолчанию, который печатает позицию, в которой объект хранится в памяти компьютера. Если ваш вывод выглядит примерно так:

# <объект main.Elevator по адресу 0x7ff6a9ff3fd0>

# Затем вам нужно будет добавить специальный метод str, который возвращает строку, которую вы хотите напечатать. Повторяйте попытку, пока не получите желаемый результат: «Текущий этаж: 5».

# Как только вы успешно получите желаемый результат, вы закончите работу с этой тетрадью для упражнений. Потрясающий!
