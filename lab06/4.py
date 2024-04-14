list = []
while True:
    a = input('nhap du lieu:')
    if a == 0:
        break
    list.append(a)

#chen them phan tu
b = [1,2,3]
list.insert(0,b)
list.insert(5,b)
list.insert(-1,b)
print(list)

#xoa phan tu
k = int(input('nhap thu tu trong danh sach:'))
del a[k]
print(list)

#sap xep 
list.sort()
print(list)
list.sort(reverse = True)
print(list)
