print('Компьютер загадал целое число от 1 до 10.\nУ вас есть три попытки. Удачи!')
import random
number = random.randint(1, 10)
i = 0
while i <= 2:
    guess = input('Попробуйте угадать (для прекращения игры введите Выход): ')
    if guess == 'Выход':
        print('Game over!')
        break
    elif int(guess) == number:
        print('Победа!')
        break
    elif i == 2:
              print('Game over!\nЗагаданное число: ', number)
              break
    else:
        i = i + 1
        if int(guess) > number:
            print('Попробуйте число меньше!')
        else:
            print('Попробуйте число больше!')
