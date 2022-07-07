# Напишите код, чтобы предоставленный код с ошибками работал с использованием try/except. Если коды не работают в попытке, добавьте к списку attempt строку «Ошибка».


full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml',
            'nop', 'qr', 's', 'tv', 'wxy', 'z']

attempt = []

for elem in full_lst:
    try:
        attempt.append(elem[1])
    except:
        attempt.append("Error")
print(attempt)
