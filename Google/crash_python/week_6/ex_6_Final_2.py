# Привет, кодеры! Ниже у нас есть код, похожий на то, что мы написали в прошлом видео. Идем дальше и запускаем следующую ячейку, которая определяет наши методы get_event_date, current_users и generate_report.

def get_event_date(event):
    return event.date


def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout" and event.user in machines[event.machine]:

            machines[event.machine].remove(event.user)
    return machines


def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

# При запуске определений пользовательских функций, приведенных выше, не должно генерироваться никаких выходных данных. Чтобы убедиться, что наш код делает все, что от него требуется, нам нужен класс Event. Код в следующей ячейке ниже инициализирует наш класс Event. Идите вперед и запустите эту ячейку дальше.


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


# Хорошо, у нас есть класс Event, который имеет конструктор и устанавливает необходимые атрибуты. Далее давайте создадим несколько событий и добавим их в список, запустив следующую ячейку.

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]
# Теперь у нас куча событий. Давайте передадим эти события в нашу функцию custom_users и посмотрим, что произойдет.
users = current_users(events)
print(users)

# О, о. Код в предыдущей ячейке выдает сообщение об ошибке. Это связано с тем, что в нашем списке событий есть пользователь, который вышел из системы, на которой он не был зарегистрирован. Вы видите, что это за пользователь? Внесите изменения в первую ячейку, содержащую определения наших пользовательских функций, чтобы посмотреть, сможете ли вы исправить это сообщение об ошибке. Может быть более одного способа сделать это.

# Помните, что когда вы закончите вносить свои изменения, повторно запустите эту ячейку, а также ячейку, которая передает список событий в нашу функцию custom_users, чтобы увидеть, было ли исправлено сообщение об ошибке. Как только сообщение об ошибке будет устранено и вы правильно выведете словарь с именами машин в качестве ключей, ваши пользовательские функции будут правильно завершены. Большой!

# Теперь попробуйте создать отчет, запустив следующую ячейку.
generate_report(users)
# Воу-воу! Успех! Сообщение об ошибке было удалено, и желаемый результат был получен. Вы все сделали с этой тренировочной тетрадью. Путь!
