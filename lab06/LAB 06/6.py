import random

list =[]
for _ in range(1000):
    a = random.randint(1, 99999)
    list.append(a)
print(list)
list.sort()
print(list)
    