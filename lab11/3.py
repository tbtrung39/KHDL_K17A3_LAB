with open('lab11/f_in.dat','r') as file:
    data = list(map(int,file.read().split()))
    print(data)
    a=[]
    for i in range(1,len(data)-1):
        if (data[i]> data[i-1] and data[i]>data[i+1]) or (data[i]<data[i-1] and data[i]<data[i+1]):
            a.append(data[i])
with open('lab11/f_out.dat','w') as file:
    file.write(str(len(a))+'\n')
    for i in a:
        file.write(str(i)+' ')