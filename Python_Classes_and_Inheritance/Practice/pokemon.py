# Наряду с Pokemon родительским классом мы также предоставили несколько подклассов. Напишите еще один метод в родительском классе, который будет унаследован подклассами. Назовите это opponent. Он должен возвращать тип покемона, против которого текущий тип слаб и силен, в виде кортежа.

# Трава слаба против Огня и сильна против Воды.

# Призрак слаб против Тьмы и силен против Психического.

# Огонь слаб против Воды и силен против Травы.

# Полет слаб против электричества и силен против боя.

# Например, если p_typeподкласс равен 'Grass', .opponent()должен вернуть кортеж('Fire', 'Water')

class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"

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

    def opponent(self):
        if self.p_type == "Grass":
            return ('Fire', 'Water')
        if self.p_type == "Ghost":
            return ('Dark', 'Psychic')
        if self.p_type == "Fire":
            return ('Water', 'Grass')
        if self.p_type == "Flying":
            return('Electric', 'Fighting')

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)


class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12


class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3


class Fire_Pokemon(Pokemon):
    p_type = "Fire"


class Flying_Pokemon(Pokemon):
    p_type = "Flying"


p1 = Grass_Pokemon('Bulby')
p2 = Ghost_Pokemon('Пампкабу')
p3 = Fire_Pokemon('Char')
p4 = Flying_Pokemon('Buterfly')
print(p1.opponent())
print(p2.opponent())
print(p3.opponent())
print(p4.opponent())
