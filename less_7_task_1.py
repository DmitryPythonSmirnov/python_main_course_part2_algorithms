"""
Задача 1.
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""


import random

MIN_ITEM = -100
MAX_ITEM = 99
SIZE = 10

def reverse_sort(arr):
    n = 1
    while n < len(arr):
        swap = False  # Флаг, была ли перестановка в цикле for
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
        if swap == False:
            break  # Если не было перестановок, значит уже всё отсортировано
        n += 1
    return arr


array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # для тестирования
# array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # для тестирования

print(reverse_sort(array))
