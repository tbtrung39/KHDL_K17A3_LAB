a=[]
n=0
while True:
    i=int(input(f'nhap phan tu thứ {n+1}: '))
    if i == 0:
        break
    else:
        a.append(i)
        n+=1
a1=[i for i in a if i>0]
a2=[i for i in a if i<0]
a=a1+a2
print(f'danh sách sau khi chuyển các phần tử dương lên đầu là: {a}')
m=int(input('nhập số cần chèn: '))
a.insert(0,m)
a.insert(4,m)
a.append(m)
print(f'danh sách sau khi chèn số là: {a}')