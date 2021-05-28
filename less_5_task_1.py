"""
Задача 1.
Пользователь вводит данные о количестве предприятий, их наименования
и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""


from collections import defaultdict

companies = defaultdict(float)
QUARTERS = 4

comp_num = int(input('Введите количество предприятий: '))
for i in range(1, comp_num + 1):
    comp = input(f'Введите название {i}-го предприятия: ')
    for j in range(1, QUARTERS + 1):
        profit = float(input(f'Введите прибыль за {j}-й квартал: '))
        companies[comp] += profit

total = 0  # Суммарная прибыль всех предприятий за 4 квартала
for value in companies.values():
    total += value
avg_profit = total / comp_num  # Средняя прибыль всех предприятий за 4 квартала
print(f'Суммарная прибыль всех предприятий: {total:.2f}')
print(f'Средняя прибыль всех предприятий: {avg_profit:.2f}')
print('*' * 50)
print('Предприятия с прибылью равной или выше средней:')
for key, value in companies.items():
    if value >= avg_profit:
        print(key)
print('*' * 50)
print('Предприятия с прибылью ниже средней:')
for key, value in companies.items():
    if value < avg_profit:
        print(key)
