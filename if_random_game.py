import random
x = random.randint(1, 4) 
y = int(input('Какое число загадал компьютер? Введите целое число от 1 до 4: '))
if x == y:
    print('Победа!')
else:
    print('Повторите ещё раз!')
    if x > y:
        print('Ваше число меньше загаданного')
    else:
        print('Ваше число больше загаданного')
