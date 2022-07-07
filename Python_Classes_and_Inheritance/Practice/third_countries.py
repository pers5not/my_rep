# Следующий код пытается добавить третий элемент каждого списка conts в новый список third_countries. В настоящее время код не работает. Добавьте предложение try/except, чтобы код выполнялся без ошибок, а строка «На континенте нет 3 стран» добавлялась countries вместо ошибки.


conts = [['Spain', 'France', 'Greece', 'Portugal', 'Romania', 'Germany'], ['USA', 'Mexico', 'Canada'], ['Japan', 'China', 'Korea', 'Vietnam', 'Cambodia'], [
    'Argentina', 'Chile', 'Brazil', 'Ecuador', 'Uruguay', 'Venezuela'], ['Australia'], ['Zimbabwe', 'Morocco', 'Kenya', 'Ethiopa', 'South Africa'], ['Antarctica']]

third_countries = []

for c in conts:
    try:
        third_countries.append(c[2])
    except:
        third_countries.append('Continent does not have 3 countries')

print(third_countries)
