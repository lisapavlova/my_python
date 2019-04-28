number = input('Введите число: ')
total = 0
for i in range(len(number)):
    if not number[i].isdigit():
        continue
    else:
        if int(number[i]) % 2 == 0:
            continue
        else:
            total = total + int(number[i]) ** 2
print(total)
