def call_tel(a, b):
    if a == 343:
        return 15 * b
    elif a == 381:
        return 18 * b
    elif a == 473:
        return 13 * b
    elif a == 485:
        return 11 * b        
city_code = input('Введите код города: ')
if city_code != 343 or city_code != 381 or city_code != 473 or city_code != 485:
    print('Что это за город?')
    city_code = input('Введите код города повторно: ')
duration = input('Введите длительность переговорах в минутах: ')
if bool(duration) == False:
    print('Вы не ввели длительность переговоров')
    duration = input('Введите длительность переговоров в минутах повторно: ')
print('Стоимость переговоров в рублях: ' + str(call_tel(int(city_code),float(duration))))
