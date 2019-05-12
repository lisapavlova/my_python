print('Введите первое число:')
while True:
    try:
        first_number = float(input())
        break
    except Exception as e:
        print(e)
print('Введите второе число:')
while True:
    try:
        second_number = float(input())
        break
    except Exception as e:
        print(e)
operators = ['+', '-', '*', '/', '^']
def my_sum(x, y):
    return x + y
def my_diff(x, y):
    return x - y
def my_mult(x, y):
    return x * y
def my_div(x, y):
    try:
        return x / y
    except Exception as e:
        return e
def my_pow(x, y):
    return x ** y
functions = {'+': my_sum, '-': my_diff, '*': my_mult, '/': my_div, '^': my_pow}
print('Введите оператор (+, -, *, /, ^):')
while True:
    operator = input()
    if not operator in operators:
        print('Выберите оператор из имеющихся!')
        continue
    else:
        break
print(functions[operator](first_number, second_number))
