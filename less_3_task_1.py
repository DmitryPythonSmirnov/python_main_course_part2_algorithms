"""
Задача 1.
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


RANGE_START = 2  # Первое число проверяемого диапазон
RANGE_STOP = 10  # Последнее число проверяемого диапазона
START_NUMBER = 2
STOP_NUMBER = 9

# Список для хранения счётчиков, напр. count_lst[2] - кол-во чисел, кратных 2
# Индекс совпадает с числом, на кратность которому проверяем, чтобы не запутаться
# В этом случае count_lst[0] и count_lst[1] всегда будут 0
# Заполняем массив нулями
count_lst = [0 for i in range(10)]

for i in range(RANGE_START, RANGE_STOP + 1):
    for j in range(START_NUMBER, STOP_NUMBER + 1):
        if i % j == 0:
            count_lst[j] += 1

for j in range(START_NUMBER, STOP_NUMBER + 1):
    print(f'Количество чисел, кратных {j}: {count_lst[j]}')
