# Используя метод форматирования, заполните пробелы в функции convert_distance, чтобы она возвращала фразу «X миль равно Y км», где Y имеет только 1 десятичный знак. Например, convert_distance(12) должен вернуть «12 миль равно 19,2 км».
def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km
