a=[]
n=0
while True:
    i=int(input(f'Nhập phần tử thứ {n+1}: '))
    if i == 0:
        break
    else:
        a.append(i)
        n+=1
a.insert(0,[1,2,3])
a.append([1,2,3])
a.insert(4,[1,2,3])
print(f'Danh sách sau khi chèn: {a}')
#
k=int(input('nhập k: '))
del a[k-1]
print(f'Danh sách sau khi xóa bỏ vị trí thứ {k} là: {a}')
#
a.sort()
print(f'Danh sách sau khi sắp xếp tăng dần: {a}')
#
a.sort(reverse=True)
print(f'Danh sách sau khi sắp xếp giảm dần: {a}')