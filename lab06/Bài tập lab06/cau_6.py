import random
a = []
while len(a) < 1000:
    num = random.randint(1, 9999)
    if num not in a:
        a.append(num)
print(a)
# 
x = sorted(a)
print(x)
# 
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            tmp = a[j]
            a[j] = a[i]
            a[i] = tmp
print(a)
