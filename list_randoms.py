#Создайте список из случайных чисел. Найдите количество различных элементов в нем.

import random
try:
    list_rand = [random.randint(0, 9) for i in range(int(input('Введите количество элементов списка: ')))]
    print(list_rand)
    print(len(set(list_rand)))
except:
    print('Ошибка ввода! Начните сначала!')