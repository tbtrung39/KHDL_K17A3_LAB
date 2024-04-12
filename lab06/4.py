
a=[]
n=0
while True:
    i=int(input(f'nhap phan tu thứ {n+1}: '))
    if i == 0:
        break
    else:
        a.append(i)
        n+=1
a.insert(0,[1,2,3])
a.append([1,2,3])
a.insert(4,[1,2,3])
print(f'danh sách sau khi chèn: {a}')
k=int(input('nhập k: '))
del a[k-1]
print(f'danh sách sau khi xóa bỏ vị trí thứ {k} là: {a}')
