"""
Задача 6.
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""


import random

SIZE = 10
MIN_ITEM = -100
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

print(f'Минимальный элемент: {min_item}')
print(f'Максимальный элемент: {max_item}')

if min_item_idx > max_item_idx:
    min_item_idx, max_item_idx = max_item_idx, min_item_idx

summ = 0
for i in range(min_item_idx + 1, max_item_idx):
    summ += arr[i]

print(f'Сумма элементов, находящихся между минимальным и максимальным элементами: {summ}')
