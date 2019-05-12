import json    
try:
    with open('tasks.json') as task_file:
        task = json.load(task_file)
        print('Текущие задачи из файла:')
        for i in range (0, len(task)):
            print('Задача: ',task[i]['name'] ,' Категория: ', task[i]['category'] , ' Время: ', task[i]['time'])
except Exception as e:
        print(e)
while True:
    print('Простой todo:\n    1. Добавить задачу.\n    2. Вывести список задач.\n    3. Выход.')
    choice = input('Укажите число: ')
    if choice == '3':
        try:
            with open('tasks.json', 'w') as task_file:
                json.dump(task, task_file)
        except Exception as e:
            print(e)
        print('Задачи сохранены в файл!')
        break
    elif choice == '1':
        task.append(dict())
        task[-1]['name'] = (input('Сформулируйте задачу: '))
        task[-1]['category'] = (input('Добавьте категорию к задаче: '))
        task[-1]['time'] = (input('Добавьте время к задаче: '))
    elif choice == '2':
        for i in range (0, len(task)):
            print('Задача: ',task[i]['name'] ,' Категория: ', task[i]['category'] , ' Время: ', task[i]['time'])

