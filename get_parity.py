def parity(x):
    if x % 2 == 0:
        print('Это число чётное')
    else:
        print('Это число нечётное')
number = int(input('Введите проверяемое число: '))
parity(number)
