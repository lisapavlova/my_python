names = ['John', 'Paul', 'George', 'Ringo']
for i in reversed(names):
    if i != 'John' and i != 'Paul':
        names.remove(i)
print(names)
