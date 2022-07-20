def func(string, number, lis, num_float):
    if type(string) == str:
        print(string)
    if type(number) == int:
        print(number)
    if type(lis) == list:
        print(lis)
    if type(num_float) == float:
        print(num_float)
        print()
        print("string: {}\nnumber:{}\nlist: {}\nfloat: {}".format(string, number, lis, num_float))
        print()
    # return это возвращаемое знаечение функции - тоесть то что она возвращает можно использовать в другой функции
    return number
    
    
# Параметры указанные в переменных
string_1 = 'abc'
number_2 = 123
list_3 = ['a', 1, 1.23]
num_float_4 = 1.23
# При вызове функции задаем переменные
func(string_1, number_2, list_3, num_float_4)
print()


# Параметры которые указываем при вызове функции
# 1 - string = 'cba', 2 - number = 321, 3 - list = [1.23, 1, 'a'],  4 - num float = 32.1
# порядок задаваемый при вызове функции соотвествует порядку указаных параметров
# 1 - string 
# 2 - number 
# 3 - list 
# 4 - float
func('cba', 321, [1.23, 1, 'a'], 32.1)
print()


# Можно задавать значения по именам параметров тогда порядок не важен
func(string='abc', num_float=2.22, number=55, lis=['abc', 2.25, 3])


# возвращаемое значение можно использовать в другой функции
def func_1(func):
    if type(func) == int:
        return f"Распечатываем number из первой функции {func}"
    # Возвращаем number возведенный в квадрат
    return func ** 2

# cохраняем функцию func в переменную parametrs
parametrs = func(string='abc', num_float=2.22, number=55, lis=['abc', 2.25, 3])

# передеаем parametrs в функцию func_1()
func_1(parametrs)
print()

# Выводим значение которое возвращает func_1() тобеж число в квадрате 
print(func_1(parametrs))