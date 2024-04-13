
import random

a=[]
for i in range(1000):
    a.append(random.randint(1,99999))
sorted(a)
a.sort()
print(a)