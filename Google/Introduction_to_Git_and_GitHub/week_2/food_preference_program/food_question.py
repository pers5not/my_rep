#!/usr/bin/env python3

# Словарь для отслеживания предпочтений в еде
counter = {}

# Откройте журнал любимых блюд и подсчитайте частоты, используя словарь
with open("favorite_foods.log", "r") as f:
    for line in f:
        food_item = line.strip()
        if food_item not in counter:
            counter[food_item] = 1
        else:
            counter[food_item] += 1

# Распечатайте все доступные понравившиеся продукты
print("Select your favorite food below:")
for item in counter:
    print(item)

# Спросите, какая еда является любимой у пользователя
answer = input("Which of the foods above is your favorite? ")
answer = answer.lower()

# Распечатать, сколько других любит любимую еду пользователя, иначе сказать, что она не может быть найдена
try:
    print("{} of your friends like {} as well!".format(
        counter[answer], answer))
    exit(0)
except KeyError:
    print("Hmm we couldn't find anyone who also likes \"{}\".".format(answer))
    print("Did you enter one of the foods listed above?")
    exit(0)
