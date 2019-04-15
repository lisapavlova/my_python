number = input('Введите атомный номер элемента: ')
if number:
    if int(number) == 3:
        print('Li')
    elif int(number) == 25:
        print('Mn')
    elif int(number) == 80:
        print('Hg')
    elif int(number) == 17:
        print('Cl')
    else:
        print('Что это за элемент?')
else:
    print('Введите атомный номер элемента!')
