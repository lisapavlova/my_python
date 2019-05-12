import random
lst = [random.randint(-100000, 100000) for i in range(1, 1000)]
counter = 0
for i in lst:
    if i < 0 and i >= min(lst) and i <= max(lst):
        counter += 1
print(counter)
