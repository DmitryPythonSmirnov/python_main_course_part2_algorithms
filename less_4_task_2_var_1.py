"""
Задача 2.
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
"""

"""
Вариант 1.
Решето Эратосфена.
"""

import timeit
import cProfile

def sieve(n):
    """Классический вариант решета Эратосфена"""
    a = [i for i in range(n)]
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j += m
        m += 1
    return a

# Задача оценки необходимого размера решета Эратосфена через математические формулы мне показалась сложной,
# не смог её решить (частота простых чисел уменьшается при движении по шкале натуральных чисел вправо,
# то есть простые числа встречаются всё реже, значит, размер решета нужен всё больше),
# поэтому решил обойтись просто диапазонами и ограничением на максимальный порядковый номер простого числа.
# Диапазоны взял из таблицы: https://ru.wikipedia.org/wiki/Функция_распределения_простых_чисел
def main(num):
    if num <= 4:
        limit = 10
    elif num <= 25:
        limit = 100
    elif num <= 168:
        limit = 1_000
    elif num <= 1_229:
        limit = 10_000
    elif num <= 9_592:
        limit = 100_000
    elif num <= 78_498:
        limit = 1_000_000
    elif num <= 664_579:
        limit = 10_000_000
    else:
        return 'Слишком большое число'

    full_list = sieve(limit)  # Полное решето с нолями
    prime_list = [i for i in full_list if i != 0]  # Список из простых чисел
    return prime_list[num - 1]


# if __name__ == '__main__':
#     print(main(5))


print(timeit.timeit('main(50)', number=1000, globals=globals()))   # 0.6430146999999999
print(timeit.timeit('main(100)', number=1000, globals=globals()))  # 0.5537509
print(timeit.timeit('main(150)', number=1000, globals=globals()))  # 0.5701892000000002
print(timeit.timeit('main(200)', number=1000, globals=globals()))  # 6.5780008
print(timeit.timeit('main(600)', number=1000, globals=globals()))  # 6.6892564
print(timeit.timeit('main(1000)', number=1000, globals=globals())) # 6.7058019999999985
print(timeit.timeit('main(1300)', number=1000, globals=globals())) # 75.53205059999999
print(timeit.timeit('main(5000)', number=1000, globals=globals())) # 74.1593658

cProfile.run('main(5000)')
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    0.098    0.098 <string>:1(<module>)
#      1    0.079    0.079    0.092    0.092 less_4_task_2_var_1.py:23(sieve)
#      1    0.013    0.013    0.013    0.013 less_4_task_2_var_1.py:25(<listcomp>)
#      1    0.000    0.000    0.096    0.096 less_4_task_2_var_1.py:42(main)
#      1    0.004    0.004    0.004    0.004 less_4_task_2_var_1.py:61(<listcomp>)
#      1    0.000    0.000    0.098    0.098 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
Выводы:
1. В пределах одного диапазона функция является константой - O(1), так как
размер решета один и тот же. Как только переходим в следующий диапазон,
получаем скачок по времени Примерно в 10 раз, так как размер решета
увеличивается в 10 раз.

2. По cProfile видно, что все функции вызываются 1 раз, наибольшее время
тратиться на функцию sieve(n).
"""
