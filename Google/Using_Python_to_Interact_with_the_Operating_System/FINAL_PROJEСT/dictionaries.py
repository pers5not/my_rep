import operator

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
print(sorted(fruit.items()))

print(sorted(fruit.items(), key=operator.itemgetter(1)))
print(sorted(fruit.items(), key=operator.itemgetter(1), reverse=True))
