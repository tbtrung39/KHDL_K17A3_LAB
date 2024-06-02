with open('lab11/Phieu_Diem.txt','r',) as f1:
    a = [i.strip('\n').split(',') for i in list(f1.readlines())]
with open('lab11/Sbd_Ten.txt','r',encoding='utf-8') as f2:
    b = [ i.strip('\n').split(',') for i in list(f2.readlines())]
with open('lab11/Sbd_Ph.dat','r') as f3:
    c = [ i.strip('\n') for i in list(f3.readlines())]
for i in range(len(b)):
    b[i].append(a[i][1])
print(b)
b1=sorted(b,key = lambda x: float(x[2]),reverse= True)
with open('lab11/Ketqua.txt','w',encoding='utf-8') as f4:
    for i in b1:
        f4.write(' '.join(map(str,i))+'\n')
