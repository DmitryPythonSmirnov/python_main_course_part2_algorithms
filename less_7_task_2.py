"""
Задача 2.
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
import random

MAX_ITEM = 50
SIZE = 10


def merge_sort(arr):
    if len(arr) == 0:
        return 'Передали пустой массив.'
    if len(arr) == 1:
        return arr
    left_arr = arr[:len(arr) // 2]    # Делим на два массива,
    right_arr = arr[len(arr) // 2:]   # правый и левый
    left_arr = merge_sort(left_arr)   # Для каждого снова вызываем функцию сортировки
    right_arr = merge_sort(right_arr) # Для каждого снова вызываем функцию сортировки
    new_arr = []  # Пустой массив, в который будем добавлять элементы из правого и левого массива
    i_left = 0
    i_right = 0
    while i_left < len(left_arr) and i_right < len(right_arr):
        if left_arr[i_left] <= right_arr[i_right]:
            new_arr.append(left_arr[i_left])
            i_left += 1
        else:
            new_arr.append(right_arr[i_right])
            i_right += 1

    if i_left == len(left_arr):   # Если закончился левый массив,
        new_arr.extend(right_arr[i_right:]) # тогда к new_arr добавляем остаток правого массива
    else:
        new_arr.extend(left_arr[i_left:])  # иначе к new_arr добавляем остаток левого массива
    return new_arr


array = [random.random() * 50 for _ in range(SIZE)]
print(array)

print(merge_sort(array))
