def csv_from_list(file, lst):
    if file.endswith('.csv'):
        try:
            with open(file, 'x') as csvfile:
                csvfile.write('name,adress,age')
                for i in lst:
                    csvfile.write('\n')
                    for j in i:
                        csvfile.write(j)
                        if i.index(j) < 2:
                            csvfile.write(',')
        except Exception as e:
            print(e)
    else:
        print('Укажите название файла в формате .csv')
# csv_from_list('new.csv', [('Георгий', 'Невский проспект', '22'), ('Иван', 'пр. Ветеранов', '21')])
# csv_from_list('new.txt', [('Георгий', 'Невский проспект', '22'), ('Иван', 'пр. Ветеранов', '21')])
