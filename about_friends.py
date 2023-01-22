# Еще немного о друзьях
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Выведите средний возраст всех друзей и самое длинное имя.

sum_age = 0
y = 0
count = 0
frends = []
for i in range(int(input('Введите количество друзей: '))):
    frend_dict = {'name': input('Введите имя друга: '), 'age': input('Введите возраст друга: ')}
    frends.append(frend_dict)
print(frends)
x_list = (list([values for frend_dict in frends for values in frend_dict.values()]))
for el in x_list:
    if el.isnumeric():
        sum_age += int(el)
        count += 1
    else:
        if len(el) > y:
            y = len(el)
            z = el
print('Средний возраст друзей: ', round(sum_age/count), '\nСамое длинное имя: ', z)
