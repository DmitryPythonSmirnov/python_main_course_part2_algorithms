"""
Задача 2.
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


from collections import deque

HEX_STR = '0123456789ABCDEF'
BASE = 16


def increase_len(deq, max_len):
    """Функция добавляет в очередь deq ноли слева до суммарной длины очереди max_len"""
    for _ in range(max_len - len(deq)):
        deq.appendleft('0')


def sum_hex(deq1, deq2):
    """Функция склаыдвает два 16-ричных числа"""
    if len(deq1) > len(deq2):
        max_len = len(num_1)
        increase_len(deq2, max_len)  # Добавляем ноли сдева в deq2
    elif len(deq1) < len(deq2):
        max_len = len(deq2)
        increase_len(deq1, max_len)  # Добавляем ноли сдева в deq1
    else:
        max_len = len(deq1)

    result = deque()
    increment = 0
    for i in range(max_len):
        idx = HEX_STR.index(deq1.pop().upper()) + HEX_STR.index(deq2.pop().upper()) + increment
        if idx <= BASE - 1:
            result.appendleft(HEX_STR[idx])
            increment = 0
        else:
            result.appendleft(HEX_STR[idx - BASE])
            increment = 1
    # Если после выхода из цикла осталась переходная единица, её нужно добавить слева
    if increment == 1:
        result.appendleft('1')
    return list(result)


num_1_orig = deque(input('Введите первое 16-ричное число: '))
num_2_orig = deque(input('Введите второе 16-ричное число: '))

# Делаю копии, чтобы сохранить оригинал на всякий случай, напр., для умножения,
# но до умножения в итоге не дошёл
num_1 = num_1_orig.copy()
num_2 = num_2_orig.copy()

print(f'Сумма чисел: {sum_hex(num_1, num_2)}')
