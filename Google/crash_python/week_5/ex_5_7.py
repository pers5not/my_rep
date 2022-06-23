# В этом упражнении мы создадим несколько классов для имитации сервера, принимающего соединения извне, а затем балансировщик нагрузки, который гарантирует наличие достаточного количества серверов для обслуживания этих соединений.

# Чтобы представить серверы, которые заботятся о соединениях, мы будем использовать класс Server. Каждое соединение представлено идентификатором, который может быть, например, IP-адресом компьютера, подключающегося к серверу. Для нашей симуляции каждое соединение создает случайную нагрузку на сервер от 1 до 10.

# Запустите следующий код, который определяет этот класс сервера.
#Begin Portion 1#
import random


class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Добавляем соединение в словарь с расчетной нагрузкой
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Удалить соединение из словаря
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Суммируем нагрузку для каждого соединения
        for load in self.connections.values():
            total += load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

#End Portion 1#
# Теперь запустите следующую ячейку, чтобы создать экземпляр сервера и добавить к нему соединение, а затем проверьте загрузку:


server = Server()
server.add_connection("192.168.1.1")

print(server.load())

# # Вернитесь к определению класса Server и заполните недостающие части для методов add_connection и load, чтобы ячейка выше печатала число, отличное от нуля. Поскольку нагрузка рассчитывается случайным образом, это число должно быть разным при каждом выполнении кода.

# # Подсказка: помните, что вы можете перебирать значения словаря соединений точно так же, как любую последовательность.

# # Большой! Если ваш вывод представляет собой случайное число от 1 до 10, вы успешно закодировали методы add_connection и load класса Server. Отличная работа!

# # Как насчет закрытия соединения? Прямо сейчас метод close_connection ничего не делает. Вернитесь к определению класса Server и заполните недостающий код для метода close_connection, чтобы следующий код работал правильно:

server.close_connection("192.168.1.1")
print(server.load())

# # Вы успешно написали метод close_connection, если ячейка выше выводит 0.

# # Подсказка: помните, что del словарь[ключ] удаляет элемент с ключевым ключом из словаря.

# # Хорошо, теперь у нас есть базовая реализация класса сервера. Давайте посмотрим на базовый класс LoadBalance. Этот класс начнется только с одним доступным сервером. Когда соединение будет добавлено, оно случайным образом выберет сервер для обслуживания этого соединения, а затем передаст соединение на сервер. Класс LoadBalancing также должен отслеживать текущие подключения, чтобы иметь возможность закрыть их. Это основная структура:

# #Begin Portion 2#


class LoadBalancing:
    def __init__(self):
        """Инициализировать систему балансировки нагрузки с одним сервером"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Случайным образом выбирает сервер и добавляет к нему соединение."""
        server = random.choice(self.servers)
       # Добавляем соединение в словарь с выбранным сервером
        server.add_connection(connection_id)
        # Добавляем подключение к серверу
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Узнать правильный сервер
        # Закрыть соединение на сервере
        # Удалить соединение из балансировщика нагрузки
        for server in self.servers:
            if connection_id in server.connections:
                server.close_connection(connection_id)
                break

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Суммируем нагрузку каждого сервера и делим на количество серверов
        total_load = 0
        total_server = 0
        for server in self.servers:
            total_load += server.load()
            total_server += 1
        return total_load/total_server

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
# #End Portion 2#

# # Как и в случае с классом Server, этот класс в настоящее время не завершен. Вам нужно заполнить пробелы, чтобы заставить его работать правильно. Например, этот фрагмент должен создать соединение в балансировщике нагрузки, назначить его работающему серверу, а затем нагрузка должна быть больше нуля:


l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

# # После запуска приведенного выше кода вывод равен 0. Заполните недостающие части для методов add_connection и avg_load класса LoadBalancing, чтобы напечатать правильную нагрузку. Прежде чем продолжить, убедитесь, что средняя нагрузка балансировщика нагрузки больше 0.

# # Что, если мы добавим новый сервер?
l.servers.append(Server())
print(l.avg_load())

# # Средняя нагрузка теперь должна быть вдвое меньше, чем раньше. Если это не так, убедитесь, что вы правильно заполнили недостающие пробелы для методов add_connection и avg_load, чтобы этот код работал правильно.

# # Подсказка. Вы можете выполнить итерацию по всем серверам в списке self.servers, чтобы получить общую величину нагрузки на сервер, а затем разделить на длину списка self.servers, чтобы вычислить среднюю величину нагрузки.

# # Фантастика! А как насчет закрытия соединения?

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

# # Заполните код класса LoadBalancing, чтобы нагрузка возвращалась к нулю после закрытия соединения.

# # Отличная работа! Раньше мы добавляли сервер вручную. Но мы хотим, чтобы это происходило автоматически при средней загрузке более 50%. Чтобы сделать это возможным, заполните отсутствующий код для метода sure_availability и вызовите его из метода add_connection после добавления соединения. Вы можете протестировать его с помощью следующего кода:

for connection in range(20):
    l.add_connection(connection)
print(l)

# # Приведенный выше код добавляет 20 новых подключений, а затем выводит нагрузки для каждого сервера в балансировщике нагрузки. Если вы написали код правильно, новые серверы должны были добавляться автоматически, чтобы средняя загрузка всех серверов не превышала 50%.

# # Запустите следующий код, чтобы убедиться, что средняя нагрузка балансировщика нагрузки не превышает 50%.
print(l.avg_load())
