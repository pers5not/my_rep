# Предоставлен глючный цикл for, который пытается собрать некоторые значения из некоторых словарей. Вставьте try/except, чтобы код прошел. Если ключа нет, инициализируйте его в словаре и установите значение равным нулю.

di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {
    "Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except:
        diction["Puppies"] = 0

print("Total number of puppies:", total)
