#!/usr/bin/env python3

# Словарь для отслеживания предпочтений в еде
counter = {}

# Откройте журнал любимых блюд и добавьте его в словарь
with open("favorite_foods.log", "r") as f:
    for i in f:
        i = i[:-1]
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

# Сортирует понравившиеся продукты в порядке убывания
sort_foods = sorted(counter.items(), key=lambda x: x[1], reverse=True)

# Распечатывает понравившиеся продукты
for i in range(len(sort_foods)):
    print("{}, {}".format(sort_foods[i][0], sort_foods[i][1]))
