# Приведенный ниже код берет список стран country и ищет их в словаре gold, который показывает некоторые страны, выигравшие золото во время Олимпийских игр. Однако этот код в настоящее время не работает. Правильно добавьте предложение try/except в код, чтобы он правильно заполнил список country_gold либо количеством выигранных золотых монет, либо строкой «Не получил золото».


gold = {"US": 46, "Fiji": 1, "Great Britain": 27,
        "Cuba": 5, "Thailand": 2, "China": 26, "France": 10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []

for x in country:
    try:
        country_gold.append(f"{x}: {gold[x]}")
    except:
        country_gold.append("Did not get gold")

print(country_gold)
