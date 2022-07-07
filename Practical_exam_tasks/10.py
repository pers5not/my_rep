# 10. Розробіть програму яка сортує список чисел за зростанням їх абсолютного значення.

import random

N = int(input("Введіть розмір списку чисел - "))

my_list_int = [random.randint(-100, 100) for num in range(N)]

print(my_list_int)

my_list_int.sort(key=lambda v: (abs(v), v))

print(my_list_int)
