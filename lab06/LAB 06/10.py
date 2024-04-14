import random
list = []
for i in range(200):
    i = random.randint(0,201) and i % 5 ==0 and i % 7 ==0
    list.append(i)
print(list)
