# Разрешения файла в системе Linux разделены на три набора по три разрешения: чтение, запись и выполнение для владельца, группы и других. Каждое из трех значений может быть выражено как восьмеричное число, суммирующее каждое разрешение, где 4 соответствует чтению, 2 — записи и 1 — выполнению. Или это может быть написано строкой с использованием букв r, w и x или - когда разрешение не предоставлено.
#  Например:
#  640 — чтение/запись для владельца, чтение для группы и отсутствие разрешений для остальных; преобразуется в строку, это будет: "rw-r-----"
#  755 — чтение/запись/выполнение для владельца и чтение/выполнение для группы и других; преобразуется в строку, это будет: "rwxr-xr-x"
#  Заполните пробелы, чтобы код преобразовал разрешение в восьмеричном формате в строковый формат.
def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for i in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if i >= value:
                result += letter
                i -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------
