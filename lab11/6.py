with open('lab11/bai6.txt','r',) as f:
    data =[]
    for i in f:
        row = list(map(int,i.split()))
        data.append(row)
    print(data)
print(f'dòng đầu :{data[0]} \ndòng thứ 3: {data[3]}')
print('hiển thị toàn bộ file')
for i in data:
    for j in i:
        print(str(j).ljust(5),end='')
    print()
a=[[0 for i in range(4)] for j in range(4)]
data[0]=[4,0,0,0]

for i in range(len(a)):
    for j in range(len(a)):
        if data[i][j]%2!=0:
            a[i][j]=data[i][j]
with open('lab11/OOD.txt','w') as f1:
    for i in a:
        f1.write(' '.join(map(str,i))+'\n')
with open('lab11/OOD.txt','r') as f2:
    data1=list(f2.readlines())
    print('nội dung dòng cuối của file OOD.txt:')
    print(data1[3])