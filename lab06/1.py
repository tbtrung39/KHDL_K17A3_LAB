a = [2,-4,1,9,-3,6,3,-2,6,8]
# tinh tong cac phan tu trong danh sach
tong = 0
for i in a:
    tong +=i
print(f'tong cac so la {tong}')

# dem so duong va tong cac so duong
count = 0
tong_duong = 0
for c in a:
    if i>0:
        count+=1
        tong_duong+= c
print(f'so cac phan tu la so duong la {count} va tong cac so duong la {tong_duong}')

#tim vi tri cua phan tu am dau tien trong danh sach
for am in a:
    if am < 0:
        print(f'phan tu am dau tien trong list la : {am}')
        break

#tim vi tri cua phan tu duong cuoi cung trong danh sach
a.reverse()
for i in a:
    if i>0:
        print(f'phan tu duong cuoi cung trong list la: {i}')
    break

#tim phan tu lon nhat trong danh sach va vi tri cuoi cung 
a.reverse()
print(a)
max = 0
while True:
    for i in range (0,len(a)):
        if a[i] >max:
            max = a[i]
print(f'phan tu lon nhat cua danh sach la {max} va vi tri cua phan tu la {i}')