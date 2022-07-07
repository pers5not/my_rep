# Приведенный ниже код с ошибками выводит значение вида спорта в списке sport. Используйте try/except, чтобы код работал правильно. Если вида спорта нет в словаре ppl_play, добавьте его со значением 1.

sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]

ppl_play = {"hockey": 4, "soccer": 10, "football": 15, "tennis": 8}
new_ppl = dict()
new_ppl1 = dict()
for x in sport:
    try:
        print(ppl_play[x])
    except:
        ppl_play[x] = 1

# Сортировка по ключу
lst1 = sorted([(k, v) for k, v in ppl_play.items()])
sorted_dict = {k: v for k, v in lst1}
# for k, v in lst1:
#     new_ppl1[k] = v
# print(f"Сортировка по ключу - { new_ppl1}")
print(f"Сортировка по ключу - {sorted_dict}")
# =======================================================================================
lst = sorted([(k, v) for v, k in ppl_play.items()])
sorted_dict1 = {k: v for v, k in lst}
# for k, v in lst:
#     new_ppl[v] = k
# print(f"Сортировка по значению - {new_ppl}")
print(f"Сортировка по значению - {sorted_dict1}")


# a = sorted(ppl_play)
# sorted_tuples = sorted(ppl_play.items(), key=lambda item: item[1])
# sorted_dict = {k: v for k, v in sorted_tuples}

# print(new_ppl)
# print(sorted_dict)
