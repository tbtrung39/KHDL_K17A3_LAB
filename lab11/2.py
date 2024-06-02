with open('lab11/Inp.txt','r') as file:
    data = list(map(int,file.read().split()))
    data.sort()
with open('lab11/out.dat','w') as file:
    for i in data:
        file.write(str(i)+' ')
