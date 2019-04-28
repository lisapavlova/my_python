number = 0
total = 0
while True:
    number = input('Введите целое число или Стоп для выхода: ')
    if number == 'Стоп':
        break
    elif not number.isdigit():
        print('Ошибка ввода.')
        continue
    else:
        total = total + int(number)
print(total)
