tasks = []
while True:
    print('Простой todo:\n    1. Добавить задачу.\n    2. Вывести список задач.\n    3. Выход.')
    choice = input('Укажите число: ')
    if choice == '3':
        break
    elif choice == '1':
        tasks.append({'name':input('Сформулируйте задачу: '), 'category':input('Добавьте категорию к задаче: '), 'time':input('Добавьте время к задаче: ')})
    elif choice == '2':
        from pprint import pprint
        pprint(tasks)


