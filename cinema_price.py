film = input('Сейчас в прокате три фильма:\n 1 - "Пятница"\n 2 - "Чемпионы"\n 3 - "Пернатая банда"\nВведите номер выбранного фильма: ')
date = input('Введите желаемую дату - сегодня или завтра: ')
time = input('Введите желаемое время (в часах): ')
tickets = input('Введите требуемое количество билетов: ')
price = int(tickets)
if date == 'завтра':
    price = price * 0.95 
if int(tickets) >= 20:
    price = price * 0.8
if film == '1':
    if time == '12':
        print('Стоимость ваших билетов: ' + str(price * 250))
    elif time == '16':
        print('Стоимость ваших билетов: ' + str(price * 350))
    elif time == '20':
        print('Стоимость ваших билетов: ' + str(price * 450))
    else:
        print('Такого сеанса нет. Перезапустите программу, выбрав фильм и время в соответствии с расписанием')
elif film == '2':
    if time == '10':
        print('Стоимость ваших билетов: ' + str(price * 250))
    elif time == '13' or time == '16':
        print('Стоимость ваших билетов: ' + str(price * 350)) 
    else:
        print('Такого сеанса нет. Перезапустите программу, выбрав фильм и время в соответствии с расписанием')
elif film == '3':
    if time == '10':
        print('Стоимость ваших билетов: ' + str(price * 350))
    elif time == '14' or time == '18':
        print('Стоимость ваших билетов: ' + str(price * 450))
    else:
        print('Такого сеанса нет. Перезапустите программу, выбрав фильм и время в соответствии с расписанием')
else:
    print('Такого фильма нет в прокате. Перезапустите программу и выберете фильм из имеющихся')

