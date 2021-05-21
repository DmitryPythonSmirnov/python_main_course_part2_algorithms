"""
Задача 7.
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""


import random

SIZE = 10  # SIZE должен быть >= 2. Считаем, что массив состоит из двух или более элементов
MIN_ITEM = -100
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)

num_1 = arr[0]
num_2 = arr[1]

for i in range(2, len(arr)):
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    if arr[i] < num_2:
        if arr[i] < num_1:
            num_2 = num_1
            num_1 = arr[i]
        else:
            num_2 = arr[i]

print(f'Два наименьших числа в массиве: {num_1} и {num_2}')
