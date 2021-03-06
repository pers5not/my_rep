# Упражнение 6. Налоги и чаевые
# Программа, которую вы напишете, должна начинаться с запроса у поль-
# зователя суммы заказа в ресторане. После этого должен быть произведен
# расчет налога и чаевых официанту. Вы можете использовать принятую
# в вашем регионе налоговую ставку для подсчета суммы сборов. В качестве
# чаевых мы оставим 18 % от стоимости заказа без учета налога. На выхо-
# де программа должна отобразить отдельно налог, сумму чаевых и итог,
# включая обе составляющие. Форматируйте вывод таким образом, чтобы
# все числа отображались с двумя знаками после запятой.

#!/usr/bin/env python3

TAX_RATE = 0.05
TIP_RATE = 0.18

total_score = float(input("Enter total score - "))


def calculation(score):
    taxes = score * TAX_RATE
    tip = score * TIP_RATE
    tax_free = score + taxes + tip
    return f"Total taxes: {taxes:.2f}$\nTotal tip: {tip:.2f}$\
        \nScore tax-free: {tax_free:.2f}$"


print(calculation(total_score))
