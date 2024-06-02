a=[]
with open("lab11\_in.dat","r") as dayso:
    listdayso=list(dayso)

for i in listdayso:
    dayso=i.split(",")

for i in dayso:
    i=int(i)
    a.append

def songto(n):
    if n <= 1:
        return False 
    for i in range(2, n):
        if n % i == 0: 
            return False
    return True
print(dayso)
print(a)
for i in a:
    if songto(i):
        print(1,i)