def read_csv(file):
    if file.endswith('.csv'):
        import csv
        try:
            with open(file, 'r') as csvfile:
                dict_reader = csv.reader(csvfile)
                lst = []
                i = 0
                for row in dict_reader:
                    lst.append([])
                    for obj in row:
                        lst[i].append(obj)
                    i += 1
                new_lst = []
                for j in range(1, len(lst)):
                    new_lst.append({})
                    for k in range(0, 3):
                        new_lst[j-1].setdefault(lst[0][k], lst[j][k])
                print(new_lst)
        except Exception as e:
            print(e)
    else:
        print('Укажите название файла в формате .csv')

# read_csv('new.csv')
