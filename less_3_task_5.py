"""
Задача 5.
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""


import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
arr = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(arr)

for i in range(len(arr)):
    if arr[i] < 0:    # Ищем первое отрицательное число
        num = arr[i]  # Инициализируем num
        idx = i       # Инициализируем idx
        # В новом цикле использую ту же самую переменную i, чтобы не создавать новой.
        # Не знаю, нормально ли так делать или плохо
        for i in range(idx + 1, len(arr)):
            if arr[i] < 0:
                if arr[i] > num:
                    num = arr[i]
                    idx = i
        print(f'Максимальный отрицательный элемент в массиве: {num}, его индекс: {idx}')
        break
else:
    print('В массиве нет отрицательных чисел')
