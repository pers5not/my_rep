from tkinter import N


cityNames = ['Detroit', 'Ann Arbor', 'Piter', 'Kharkov', 'Moscow']
popelations = [685023, 756321, 354698, 100569, 3658974]
states = ['MI', 'MI', 'UA', 'UA', 'RU']

city_tuples = zip(cityNames, popelations, states)


class City:
    def __init__(self, c, p, s) -> None:
        self.name = c
        self.population = p
        self.state = s

    def __str__(self) -> str:
        return f"{self.name} {self.state} (pop: {self.population})"


# =====================================
# cities = []
# for city_tuple in city_tuples:
#     name, pop, state = city_tuple
#     city = City(name, pop, state)
#     cities.append(city)
# print(cities)
"""ОДНО И ТОЖЕ↑↓"""
# =====================================
# cities = [City(s, p, n) for s, p, n in city_tuples]
# =====================================
cities = [City(*t) for t in city_tuples]
print(cities[1])


# lst = list(city_tuples)

# for i, j, n in city_tuples:
#     print(i, j, n)
