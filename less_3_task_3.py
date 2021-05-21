"""
Задача 3.
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""


import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)

min_item = arr[0]
max_item = arr[0]
min_item_idx = 0
max_item_idx = 0

for i in range(1, len(arr)):
    if arr[i] > max_item:
        max_item = arr[i]
        max_item_idx = i
    elif arr[i] < min_item:
        min_item = arr[i]
        min_item_idx = i

print(f'Минимальный элемент: {min_item}, его индекс: {min_item_idx}')
print(f'Максимальный элемент: {max_item}, его индекс: {max_item_idx}')
arr[min_item_idx], arr[max_item_idx] = arr[max_item_idx], arr[min_item_idx]
print('Массив после перестановки:')
print(arr)
