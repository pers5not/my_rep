import ex_4 as queue

q = queue.PrintQueue()


def name_doc():
    name = input('Введите имя - ')
    doc = input('Введите документ - ')
    return f", '{name}', '{doc}'"


print(f"""
1 - добавить содрудника в очередь
2 - показать всю очередь
3 - проверка наличия документов в очереди
4 - удаления сотрудника из очереди
0 - выход""")
print()
while True:
    user_input = input("Введите свой выбор - ")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == 1:
            print(f"""
    ВЫБЕРИТЕ ПРИОРИТЕТ

    1 - Высокий
    2 - Средний
    3 - Низкий
    """)
            prior = int(input('Выберите приоритет - '))
            if prior == 1:
                q.addEmployes(
                    f"(({queue.Priority.HIGH.value} {name_doc()}))")
            if prior == 2:
                q.addEmployes(
                    f"(({queue.Priority.NORMAL.value} {name_doc()}))")
            if prior == 3:
                q.addEmployes(
                    f"(({queue.Priority.LOW.value} {name_doc()}))")
        if user_input == 2:
            for elem in q.employes:
                print(elem)
        if user_input == 3:
            print(f"Документов в очереди - {q.queueCheck()}")
        if user_input == 4:
            print(f" {q.getEmployes()} - ДОКУМЕНТ УДАЛЕН ИЗ ОЧЕРЕДИ")
        if user_input == 0:
            print(f"\nВЫ ВЫШЛИ ИЗ ПРОГРАММЫ")
            break
    else:
        print("ОШИБКА 'вы ввели не павильное значение'")
