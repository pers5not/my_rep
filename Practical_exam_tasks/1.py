# 1. Розробіть програму, яка перевіряє, чи є матриця, всі елементи якої задані випадковим чином, магічним квадратом (сума чисел у кожному рядку, кожному стовпці та обох діагоналях однакова).

import random
import numpy as np


# створюємо матрицю

def creatMatrix():

    N = int(input("Введіть розмір матриці - "))
    matrix = [[random.randint(10, 50) for i in range(N)]
              for j in range(N)]
    matrix = np.array(matrix)
    return matrix


# щитаємо рядки

def rows(square, magic_num):
    n = len(square)
    for i in range(n):
        sum_row = 0
        for j in range(n):
            sum_row += square[i][j]
        if sum_row != magic_num:
            return sum_row
    return sum_row


# щитаємо колонки

def columns(square, magic_num):
    n = len(square)
    for i in range(n):
        sum_col = 0
        for j in range(n):
            sum_col += square[j][i]
        if sum_col != magic_num:
            return sum_col
    return sum_col


# щитаємо діагональ

def diagonals(square, magic_num):
    n = len(square)
   # зліва направо
    sum_diag = 0
    for i in range(n):
        sum_diag += square[i][i]
    if sum_diag != magic_num:
        return sum_diag
    # справа наліво
    sum_diag = 0
    for i in range(n):
        sum_diag += square[i][-(i+1)]
    return sum_diag


# основна функція

def magicSquare(square):
    # ищем магическое число
    magic_constant = 0
    for n in square[0]:
        magic_constant += n
    if (rows(square, magic_constant) == columns(square, magic_constant) and diagonals(square, magic_constant)) == columns(square, magic_constant):
        print(f"""
Сума рядків = {magic_constant}
Сума стовпчиків = {columns(square, magic_constant)}
Сума діагоналей = {diagonals(square, magic_constant)}
Матриця є магічним квадратом""")

    else:
        print(f"""
Сума рядків = {magic_constant}
Сума стовпчиків = {columns(square, magic_constant)}
Сума діагоналей = {diagonals(square, magic_constant)}
Матриця не є магічним квадратом""")


mat = creatMatrix()
sq = [[0, 2, 4, 6],
      [6, 6, 0, 0],
      [1, 1, 5, 5],
      [5, 3, 3, 1]]
sq = np.array(sq)

print(mat)
magicSquare(mat)
print()
print(sq)
magicSquare(sq)
