a = [1,2,3,5,-5,3,-6]
a.reverse()
print(a)
max = 0
vitri = 0
while True:
    for i in range (0,len(a)):
        if a[i] >max:
            max = a[i]
            vitri = i
print(f'phan tu lon nhat cua danh sach la {max} va vi tri cua phan tu la {vitri}')