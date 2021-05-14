"""
Задача 5.
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв.
"""

letter_1 = input('Введите первую букву от "a" до "z": ')
letter_2 = input('Введите вторую букву от "a" до "z": ')
letter_1_ascii = ord(letter_1)
letter_2_ascii = ord(letter_2)
num_1 = letter_1_ascii - 96
num_2 = letter_2_ascii - 96
if num_1 > num_2:
    num_between = num_1 - num_2 - 1
else:
    num_between = num_2 - num_1 - 1

print(f'Порядковый номер буквы "{letter_1}" в английском алфавите: {num_1}')
print(f'Порядковый номер буквы "{letter_2}" в английском алфавите: {num_2}')
print(f'Число букв между буквами "{letter_1}" и "{letter_2}" в анлийском алфавите: {num_between}')