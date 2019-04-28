# на основе цикла for
lst = [2, 4, 9, 16, 25]
new_lst_for = []
for i in lst:
    new_lst_for.append(i ** 0.5)
print(new_lst_for)

# на основе функции map
new_lst_map = list(map((lambda x: x ** 0.5), lst))
print(new_lst_map)

# в виде генератора списка
new_lst_gen = [i ** 0.5 for i in lst]
print(new_lst_gen)
