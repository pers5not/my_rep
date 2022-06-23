# Функция guest_list считывает список кортежей с именем, возрастом и профессией каждого гостя вечеринки и печатает предложение «Госту X лет, и он работает как __». для каждого. Например, guest_list(('Кен', 30, "Шеф"), ("Пэт", 35, 'Адвокат'), ('Аманда', 25, "Инженер")) должен вывести: Кену 30 лет и работает шеф-поваром. Пэт 35 лет, работает юристом. Аманде 25 лет, она работает инженером. Заполните пробелы в этой функции, чтобы сделать это.#
def guest_list(guests):
    for name, age, prof in guests:
        print("{} is {} years old and works as {}".format(name, age, prof))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
            ('Amanda', 25, "Engineer")])

# Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
