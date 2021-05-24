"""
Задача 1.
Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать
(укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом
(не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""

"""
Для разбора беру задачу 4 из ПЗ к уроку 3: "Определить, какое число в массиве встречается чаще всего."
Рассматриваю 3 вариант, каждый в отдельном файле.
"""

# Вариант 1 - полный перебор по всем элементам массива arr

import random
import timeit
import cProfile

MIN_ITEM = 0
MAX_ITEM = 5
SIZE_1 = 100
SIZE_2 = 200
SIZE_3 = 300
SIZE_4 = 400
SIZE_5 = 500
SIZE_6 = 600
arr_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_1)]
arr_2 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_2)]
arr_3 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_3)]
arr_4 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_4)]
arr_5 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_5)]
arr_6 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_6)]

def func_1(arr):
    count_max = 0
    num = None
    for item_1 in arr:
        count = 0
        for item_2 in arr:
            if item_1 == item_2:
                count += 1
        if count > count_max:
            num = item_1
            count_max = count
    return num, count_max

print(timeit.timeit('func_1(arr_1)', number=1000, globals=globals()))  # 0.6336314000000001
print(timeit.timeit('func_1(arr_2)', number=1000, globals=globals()))  # 2.4680084
print(timeit.timeit('func_1(arr_3)', number=1000, globals=globals()))  # 5.6725651
print(timeit.timeit('func_1(arr_4)', number=1000, globals=globals()))  # 10.078975799999998
print(timeit.timeit('func_1(arr_5)', number=1000, globals=globals()))  # 15.9998429
print(timeit.timeit('func_1(arr_6)', number=1000, globals=globals()))  # 22.8177471

cProfile.run('func_1(arr_6)')
#       4 function calls in 0.024 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.024    0.024 <string>:1(<module>)
#      1    0.024    0.024    0.024    0.024 test.py:22(func_1)
#      1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
Выводы:
1. В функции func_1(arr) два цикла, один вложен в другой, и в каждом цикле
производится просмотр всех элементов массива, поэтому функция func_1(arr)
имеет квадратичную асимптотику - O(n^2).
Замеры с помощью timeit это подтверждают.
При увеличении длины массива в N раз время увеличивается в N^2 раз.
Если отталкиваться от первого измерения и округлить время до 0.63 секунды,
то расчётное время остальных измерений должно быть примерно следующее:
(Число слева - это N)
100 | 0.63
200 | 0.63 * 4 = 2.52   (результат измерений: 2.4680084)
300 | 0.63 * 9 = 5.67   (результат измерений: 5.6725651)
400 | 0.63 * 16 = 10.08 (результат измерений: 10.078975799999998)
500 | 0.63 * 25 = 15.75 (результат измерений: 15.9998429)
600 | 0.63 * 36 = 22.68 (результат измерений: 22.8177471)

Как видим, расчётное время практически совпадает с результатами timeit.

2. По cProfile видно, что функция func_1(arr) вызывается только 1 раз.
Других выводов по cProfile сделать нельзя.
"""
