# Упражнение 3. Площадь комнаты
# Напишите программу, запрашивающую у пользователя длину и ширину
# комнаты. После ввода значений должен быть произведен расчет площади
# комнаты и выведен на экран. Длина и ширина комнаты должны вводиться
# в формате числа с плавающей запятой. Дополните ввод и вывод единицами
# измерения, принятыми в вашей стране. Это могут быть футы или метры.

lenght, width = float(input("Enter lenght - ")), float(input('Enter width - '))
area = lenght * width
print(f"Area room = {area} sm")
