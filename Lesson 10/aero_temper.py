with open('temper.stat.txt', 'r') as file:
    temps = file.readlines()
for i in range(0, len(temps)):
    temps[i] = float(temps[i].strip())
print ('Максимальное значение: ', max(temps))
print ('Минимальное значение: ', min(temps))
print ('Среднее значение: ', sum(temps)/len(temps))
unique_temps = set(temps)
print ('Уникальных значений: ', len(unique_temps))
