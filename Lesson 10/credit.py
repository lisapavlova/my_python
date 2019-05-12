import csv
credit = dict()
try:
    with open('opendata.csv', encoding='cp1251') as csvfile:
            credit_reader = csv.reader(csvfile)
            for row in credit_reader:
                if row[0] == 'Количество заявок на потребительские кредиты' and row[2].startswith('2017'):
                    if row[1] != 'Россия' and row[1] != 'region':
                        if row[1] not in credit:
                            credit[row[1]] = 0
                        credit[row[1]] += int(row[3])
            sorted_credit = sorted(credit, key=credit.get, reverse=True)
            print(sorted_credit[0])
except Exception as e:
    print(e)

