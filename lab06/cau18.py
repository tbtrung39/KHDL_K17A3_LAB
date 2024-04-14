n=int(input('Nhập hàng: '))
m=int(input('nhập cột: '))
A=[]
for i in range(n):
    print(f'hàng {i+1}')
    a=[]
    for j in range(n):
        a.append(int(input(f'nhập A[{i+1}][{j+1}]: ')))
    A.append(a)
tong=0
for i in A:
    for j in i:
        tong+=j
print(f'tông của các phần tử trong ma trận: {tong}')