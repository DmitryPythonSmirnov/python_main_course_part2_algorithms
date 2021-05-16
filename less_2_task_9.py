"""
Задача 9.
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def summ(n):
    """Возвращает сумму цифр в числе n."""
    k = n % 10
    n = n // 10
    if n == 0:
        return k
    else:
        return k + summ(n)


if __name__ == '__main__':
    x_max = 0
    summ_max = 0
    while True:
        x = int(input('Введите натуральное число или 0 для выхода: '))
        if x == 0:
            break
        else:
            y = summ(x)
            if y > summ_max:
                summ_max = y
                x_max = x

    print(f'Число с максимальной суммой цифр: {x_max}')
    print(f'Сумма цифр в числе {x_max}: {summ_max}')
