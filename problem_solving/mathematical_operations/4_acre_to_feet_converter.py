# Упражнение 4. Площадь садового участка
# Создайте программу, запрашивающую у пользователя длину и ширину
# садового участка в футах. Выведите на экран площадь участка в акрах.
# Подсказка. В одном акре содержится 43 560 квадратных футов.

#!/usr/bin/env python3

SQFT_PER_ACRE = 43560

foot_lenght = float(input("Enter plot width - "))
foot_width = float(input("Enter plot width - "))


def area_plot(foot_lenght, foot_width):
    convert_acre = foot_lenght * foot_width / SQFT_PER_ACRE
    return convert_acre


print(area_plot(foot_lenght, foot_width))
