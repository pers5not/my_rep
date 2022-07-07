# Класс Pokemon, приведенный ниже, описывает покемона, его прокачку и развитие. Экземпляр класса — это один созданный вами покемон.
# Grass_Pokemon является подклассом, который наследует, Pokemon но изменяет некоторые аспекты, например, значения повышения отличаются.
# Для подкласса Grass_Pokemon добавьте еще один вызываемый метод action, возвращающий строку . Создайте экземпляр этого класса с as . Назначьте этот экземпляр переменной ."[name of pokemon] knows a lot of different moves!"name"Belle"p1

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)
# Измените Grass_Pokemon подкласс, чтобы сила атаки Grass_Pokemon экземпляров не менялась до тех пор, пока они не достигнут уровня 10. На уровне 10 и выше их сила атаки должна увеличиваться на attack_boost величину, на которую они обучены.

# Для проверки создайте экземпляр класса с именем as "Bulby". Назначьте экземпляр переменной p2. Создайте еще один экземпляр Grass_Pokemon класса с установленным именем "Pika"и назначьте этот экземпляр переменной p3. Затем используйте Grass_Pokemon методы для обучения p3 Grass_Pokemon экземпляра, пока он не достигнет по крайней мере уровня 10.


class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Normal"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def action(self):
        return f"{self.name} knows a lot of different moves!"

    def attack_up(self):
        if self.level < 10:
            return self.attack
        else:
            self.attack = self.attack + self.attack_boost
            return self.attack

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]


p1 = Grass_Pokemon("Belle")
p2 = Grass_Pokemon("Bulby")
p3 = Grass_Pokemon("Pika")
print(p2)
p3.train()
p3.train()
p3.train()
p3.train()
p3.train()
p3.train()
p3.train()
p3.train()
print(p3)
