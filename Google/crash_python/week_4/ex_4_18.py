# Тейлор и Рори устраивают вечеринку. Они разослали приглашения, и каждый собрал ответы в словари с именами своих друзей и количеством гостей, которых привел каждый друг. Каждый словарь представляет собой неполный список, но список Рори содержит более актуальную информацию о количестве гостей. Заполните пробелы, чтобы объединить оба словаря в один, чтобы каждый друг был указан только один раз, а количество гостей из словаря Рори имело приоритет, если имя включено в оба словаря. Затем распечатайте полученный словарь.


Rorys_guests = {"Adam": 2, "Brenda": 3, "David": 1,
                "Jose": 3, "Charlotte": 2, "Terry": 1, "Robert": 4}
Taylors_guests = {"David": 4, "Nancy": 1,
                  "Robert": 2, "Adam": 1, "Samantha": 3, "Chris": 5}
new_dict = {}


def combine_guests(guests1, guests2):
    guests2.update(guests1)

    return guests2


print(combine_guests(Rorys_guests, Taylors_guests))
