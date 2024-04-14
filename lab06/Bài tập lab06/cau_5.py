import random
a = []
while len(a) < 1000:
    num = random.randint(1, 9999)
    if num not in a:
        a.append(num)
print(a)
