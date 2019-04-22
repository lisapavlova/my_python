words = ['самовар', 'весна', 'лето']
import random
choice = random.randint(0, 2)
letter = random.randint(0, len(words[choice])-1)
word = words[choice][:letter] + '?' + words[choice][letter+1:]
print(word)
guess = input('Введите пропущенную букву: ')
if guess == words[choice][letter]:
    print('Победа!\nСлово: '+words[choice])
else:
    print('Увы! Попробуйте в другой раз.\nСлово: '+words[choice])
    
