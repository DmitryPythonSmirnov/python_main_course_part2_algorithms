"""
Задача 1.
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

x = int(input('Введите трехзначное число: '))
a = x // 100
b = (x - a*100) // 10
c = x - a*100 - b*10

summ = a + b + c
mult = a * b * c

print(f'Сумма цифр числа {x}: {summ}')
print(f'Произведение цифр числа {x}: {mult}')
