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

# Вариант 3 - с использованием коллекции Counter

# Использую постоянный массив. Специально исключил ноль, так как он занимает меньше памяти,
# чем числа от 1 до 5 (они занимают одинаковый объём памяти). Так легче оценивать результат.

import sys
from collections import Counter

arr = [3, 5, 1, 3, 4, 5, 4, 4, 2, 1, 5, 3, 2, 5, 4, 1, 3, 4, 3, 5,
       2, 5, 1, 4, 4, 3, 5, 5, 4, 1, 4, 1, 4, 2, 3, 4, 5, 5, 4, 2,
       5, 5, 1, 4, 2, 1, 5, 5, 3, 4, 5, 5, 1, 5, 1, 5, 4, 2, 5, 4,
       3, 2, 5, 2, 5, 1, 3, 1, 2, 2, 1, 4, 4, 5, 5, 3, 3, 3, 5, 5,
       4, 1, 3, 1, 3, 3, 1, 3, 4, 5, 4, 4, 2, 3, 3, 1, 2, 3, 4, 1]

res = Counter(arr)
num = res.most_common(1)[0][0]
count_max = res.most_common(1)[0][1]

# print(f'Чаще всего в массиве встречается число {num}, оно встретилось {count_max} раз(а)')

# Конец решения задачи. Далее код для подсчёта памяти.


# Функция для подсчёта памяти, занимаемой объектами некоторых типов.
# Типы объектов и варианты подсчёта занимаемой ими памяти будут добавляться
# далее по мере необходимости.
# Функция не универсальная, она выполняет свою задачу только в рамках данной задачи.
# В v2 добавил обработку словаря.
def memory_for_obj_v2(obj):
    """Возвращаем суммарную память, занимаемую объектом."""
    if isinstance(obj, (int, float, str)):
        return sys.getsizeof(obj)
    elif isinstance(obj, (list, tuple, set, frozenset)):
        total_size_of_obj_items = 0
        for item in obj:
            total_size_of_obj_items += sys.getsizeof(item)
        # Возвращаем сумму: память для самого объекта + память для всех его элементов
        return sys.getsizeof(obj) + total_size_of_obj_items
    elif isinstance(obj, dict):  # Добавил обработку словаря
        key_mem = 0
        value_mem = 0
        for key, value in obj.items():
            key_mem += memory_for_obj_v2(key)
            value_mem += memory_for_obj_v2(value)
        # Возвращаем сумму: память для словаря + память для ключей + память для значений
        return sys.getsizeof(obj) + key_mem + value_mem
    else:
        return 'Данный тип объекта не обрабатывается этой функцией.'


# Записываем все объекты, использованные в задаче, в список
all_elems = [arr, res, num, count_max]

total_mem = 0
for elem in all_elems:
    # print(memory_for_obj_v2(elem))  # Если нужно посмотреть результат по каждому элементу
    total_mem += memory_for_obj_v2(elem)

print(total_mem)  # 4240 байт

"""
Результат:
3656  # arr
528   # res - Counter
28    # num
28    # count_max
====
4240  # Итого
"""

"""
Общий вывод:

Результаты трёх вариантов:
Вариант 1.
3656  # arr
28    # count
28    # count_max
28    # num
28    # item_1
28    # item_2
====
3796  # Итого, из них 140 на само решение (не учитывая начального списка arr)

Вариант 2.
3656  # arr
868   # temp_set
28    # count
28    # count_max
28    # num
28    # item_1
28    # item_2
====
4664  # Итого, из них 1008 на само решение (не учитывая начального списка arr)

Вариант 3.
3656  # arr
528   # res - Counter
28    # num
28    # count_max
====
4240  # Итого, из них 584 на само решение (не учитывая начального списка arr)

Самый минимальный по занимаемой памяти получился вариант 1 - без использования коллекций
в самом решении, только 5 переменных типа int. Но он самый медленный, как было видно
в предыдущих тестированиях с timeit, так как происходит перебор n элементов списка
n раз, то есть асимптотика O(n^2).

Второй по занимаемой памяти - вариант с использованием Counter (вариант 3).
В нём итоговый Counter c 5-ю элементами и ключами занимает меньше памяти (528), чем промежуточное
множество temp_set c теми же 5-ю элементами без ключей (868).

Вариант 2 (с использованием множества) оказался самым затратным по памяти.
"""
