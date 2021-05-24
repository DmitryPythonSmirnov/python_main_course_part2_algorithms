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
Вариант 2.
Собственная функция.
"""

import math
import timeit
import cProfile

# Считаем, что на вход функции подаются числа больше 2
# Досточтоно проверить n на делимость на числа от 2 до кв.корня из n
def test_prime(n):
    """Возвращает True, если число простое, и False, если нет."""
    limit = math.sqrt(n)
    i = 2  # Начинаем проверять делимость n на i с двойки
    while i <= limit:
        if n % i == 0:
            return False
        else:
            i += 1
    return True

def main(num):
    if num == 1:
        return 2  # Первое просто число
    count = 1  # Счётчик простых чисел
    x = 2  # Первое просто число
    while count != num:
        x += 1
        if test_prime(x):
            count += 1
    return x


# if __name__ == '__main__':
#     print(main(5000))

print(timeit.timeit('main(50)', number=1000, globals=globals()))   # 0.24807279999999998
print(timeit.timeit('main(100)', number=1000, globals=globals()))  # 0.6837048
print(timeit.timeit('main(150)', number=1000, globals=globals()))  # 1.1410646999999998
print(timeit.timeit('main(200)', number=1000, globals=globals()))  # 1.8133472
print(timeit.timeit('main(600)', number=1000, globals=globals()))  # 8.6988889
print(timeit.timeit('main(1000)', number=1000, globals=globals())) # 18.4203263
print(timeit.timeit('main(1300)', number=1000, globals=globals())) # 27.445866
print(timeit.timeit('main(5000)', number=1000, globals=globals())) # 204.2655074

cProfile.run('main(5000)')
#       97222 function calls in 0.231 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.231    0.231 <string>:1(<module>)
#  48609    0.196    0.000    0.210    0.000 less_4_task_2_var_2.py:26(test_prime)
#      1    0.021    0.021    0.231    0.231 less_4_task_2_var_2.py:37(main)
#      1    0.000    0.000    0.231    0.231 {built-in method builtins.exec}
#  48609    0.013    0.000    0.013    0.000 {built-in method math.sqrt}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
Выводы:
1. Асимптотику функции сложно оценить.
По результатам timeit похоже на O(n * sqrt(n)).
Но частота простых чисел, насколько я понял, убывает примерно по формуле x / ln(x),
так что, наверно, в формуле где-то должен быть натуральный логарифм.

2. По cProfile видно, что для нахождения 5000-ого простого числа пришлось
перебрать 48609 чисел, и это занято больше времени, чем в варианте 1
с решетом Эратосфена.
"""