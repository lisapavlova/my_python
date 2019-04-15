def fun1(x):
    if -2.4 <= x <= 5.7:
        return x * x
    else:
        return 4
number = float(input('Введите аргумент функции: '))
print(fun1(number))
