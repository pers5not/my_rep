# Завершите сценарий, заполнив недостающие части. Функция получает имя, а затем возвращает приветствие в зависимости от того, является ли это имя «Тейлор».
def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor!"
    else:
        return "Hello there, " + name


print(greeting("Taylor"))
print(greeting("John"))
