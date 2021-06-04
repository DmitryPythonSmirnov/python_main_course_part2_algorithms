"""
Задача 3.
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random

M = 2
SIZE = 2 * M + 1
MIN_ITEM = -100
MAX_ITEM = 100


def median(arr):
    processed = []  # Список уже обработанных чисел, чтобы пропускать не проверять их снова
    for i in range(len(arr)):
        count_more = 0  # Счётчик элементов больше i-го
        count_less = 0  # Счётчик элементов меньше i-го
        count_eq = 0  # Счётчик элементов, равных i-му
        if arr[i] not in processed:
            for j in range(len(arr)):
                if i != j:  # Исключаем сравнение самого с собой
                    if arr[i] < arr[j]:
                        count_more += 1
                    elif arr[i] > arr[j]:
                        count_less += 1
                    else:
                        count_eq += 1
            processed.append(arr[i])

            # Медиану определяем по следующему условию:
            if count_more + count_eq >= count_less and count_less + count_eq >= count_more:
                # Остальные числа можно не проверять, возвращаем ответ
                return arr[i]


array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

print(f'Медиана: {median(array)}')
