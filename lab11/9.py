with open('lab11/PASSENGERS.IN','r') as file:
    n= int(file.readline())
    a=[]
    for i in range(n):
        a.append(list(map(float,file.readline().split())))
for i in range(n):
    if sum(a[i]) > 23 or len(a[i]) > 5:
        print(len(a[i]))
        print(i+1)
with open('lab11/WEIGHT.OUT','w') as f:
    for i in range(n):
        f.write(str(sum(a[i]))+'\n')
with open('lab11/CANCELLED.OUT','w') as f:
    for i in range(n):
        if sum(a[i]) > 23 or len(a[i]) > 5:
            f.write(str(i+1)+'\n')  
