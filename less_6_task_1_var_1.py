"""
Задача 1.
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.
"""

"""
Для разбора беру задачу 4 из ПЗ к уроку 3: "Определить, какое число в массиве встречается чаще всего."
Рассматриваю 3 варианта, каждый в отдельном файле.
"""

# Вариант 1 - полный перебор по всем элементам массива arr
# Если несколько чисел встретится одинаковое число раз,
# то выведется то, которое встретилось в массиве раньше.

# Использую постоянный массив. Специально исключил ноль, так как он занимает меньше памяти,
# чем числа от 1 до 5 (они занимают одинаковый объём памяти). Так легче оценивать результат.


import sys

arr = [3, 5, 1, 3, 4, 5, 4, 4, 2, 1, 5, 3, 2, 5, 4, 1, 3, 4, 3, 5,
       2, 5, 1, 4, 4, 3, 5, 5, 4, 1, 4, 1, 4, 2, 3, 4, 5, 5, 4, 2,
       5, 5, 1, 4, 2, 1, 5, 5, 3, 4, 5, 5, 1, 5, 1, 5, 4, 2, 5, 4,
       3, 2, 5, 2, 5, 1, 3, 1, 2, 2, 1, 4, 4, 5, 5, 3, 3, 3, 5, 5,
       4, 1, 3, 1, 3, 3, 1, 3, 4, 5, 4, 4, 2, 3, 3, 1, 2, 3, 4, 1]

count_max = 0
# Для count, item_1, item_2, num на всякий случай задаём начальные значения,
# чтобы не было ошибки при подсчёте памяти, если список arr будет пустой
count = 0
item_1 = None
item_2 = None
num = None
for item_1 in arr:
    count = 0
    for item_2 in arr:
        if item_1 == item_2:
            count += 1
    if count > count_max:
        num = item_1
        count_max = count

# print(f'Чаще всего в массиве встречается число {num}, оно встретилось {count_max} раз(а)')

# Конец решения задачи. Далее код для подсчёта памяти.


# Функция для подсчёта памяти, занимаемой объектами некоторых типов.
# Типы объектов и варианты подсчёта занимаемой ими памяти будут добавляться
# далее по мере необходимости.
# Функция не универсальная, не вызывает сама себя для вложенных объектов,
# она выполняет свою задачу только в рамках данной задачи.
def memory_for_obj_v1(obj):
    """Возвращаем суммарную память, занимаемую объектом."""
    if isinstance(obj, (int, float, str)):
        return sys.getsizeof(obj)
    elif isinstance(obj, (list, tuple, set, frozenset)):
        total_size_of_obj_items = 0
        for item in obj:
            total_size_of_obj_items += sys.getsizeof(item)
        # Возвращаем сумму: память для самого объекта + память для всех его элементов
        return sys.getsizeof(obj) + total_size_of_obj_items
    else:
        return 'Данный тип объекта не обрабатывается этой функцией.'


# Записываем все объекты, использованные в задаче, в список
all_elems = [arr, count, count_max, num, item_1, item_2]

total_mem = 0
for elem in all_elems:
    # print(memory_for_obj_v1(elem))  # Если нужно посмотреть результат по каждому элементу
    total_mem += memory_for_obj_v1(elem)

print(total_mem)  # 3796 байт

"""
Результат:
3656  # arr
28    # count
28    # count_max
28    # num
28    # item_1
28    # item_2
====
3796  # Итого
"""
