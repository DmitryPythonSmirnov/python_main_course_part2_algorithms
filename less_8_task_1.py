"""
Задача 1.
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
"""

# Предполагаем, что у нас нет коллизий, иначе как сохранять одинаковые хешы?


def subsrt_count(s):
    h_set = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            h_set.add(hash(s[i:j + 1]))

    # Вычитаем 1, так как при первом проходе внешнего цикла в обработку попадает вся строка s
    return len(h_set) - 1


s = 'papa'
print(subsrt_count(s))
