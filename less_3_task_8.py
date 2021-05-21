"""
Задача 8.
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""


SIZE_N = 5
SIZE_M = 3
matrix = []

# Для удобства ввода считаем номера строк и номера элементов в строках с 1
for i in range(1, SIZE_N + 1):
    line = []
    for j in range(1, SIZE_M + 1):
        line.append(int(input(f'Введите {j}-й элемент {i}-й строки: ')))
    matrix.append(line)

for line in matrix:
    summ_line = 0
    for item in line:
        summ_line += item
        print(f'{item:>7}', end='')
    print(f'   |{summ_line:>7}')
