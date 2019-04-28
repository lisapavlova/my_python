task = []
cat = []
date = []
while True:
    print('Простой todo:\n    1. Добавить задачу.\n    2. Вывести список задач.\n    3. Выход.')
    choice = input('Укажите число: ')
    if choice == '3':
        break
    elif choice == '1':
        task.append(input('Сформулируйте задачу: '))
        cat.append(input('Добавьте категорию к задаче: '))
        date.append(input('Добавьте время к задаче: '))
    elif choice == '2':
        for j in range (0, len(task)):
            print('Задача: ',task[j] ,' Категория: ', cat[j] , ' Дата: ', date[j])
