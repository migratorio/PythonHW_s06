# 2. Старший и младший
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего из друзей и выведите его имя.

# # Ввод:
# >> 3 # Количество друзей
# >> Иван
# >> 11
# >> Саша
# >> 12
# >> Леша
# >> 10
# # Вывод:
# >> Леша

try:
    frends = []
    for i in range(int(input('Введите количество друзей: '))):
        frend_dict = {'name': input('Введите имя друга: '), 'age': input('Введите возраст друга: ')}
        frends.append(frend_dict)
    print(frends)
    x = (list([values for frend_dict in frends for values in frend_dict.values()]))
    y = x.index(min(x))
    print('Самый младший -', x[y - 1])
except:
    print('Ошибка ввода! Начните сначала!')
