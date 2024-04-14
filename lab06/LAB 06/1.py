a = [2, -4, 1,9,-3,6,3,-2,6,8]
#
sum = 0
for i in a:
    sum+=1
print(f"Tong cac so trong list la:",{sum})
# Dem so luong cac so hang duong va tong cua cac so hang duong
count = 0
for i in a:
    if i>0:
        count +=1
        sum +=i
print(f"So cac phan tu hang duong la: {count} va tong no bang {sum} ")   
# tim vi tri cua phan tu dau tien trong danh sach
for i in a:
    if i < 0:
        print("Phan tu am dau tien trong list la: ",i)
    break
# tim vi tri cua phan tu duong cuoi cung trong danh sach     
a.reverse()
for i in a:
    if i>0:
        print("Phan tu duong cuoi cung trong danh sach la :", i) 
    break
# tim phan tu lon nhat trong danh sach va vi tri lon nhat cuoi cung
a.reverse()
print(a)
max = 0
vi_tri = 0
for i in range(0, len(a)):
    if a[i] > max:
        max = a[i]
        vi_tri = i
print(f'Phan tu lon nhat cua danh sach la: {max} va vi tri cua phan tu lon nhat la: {vi_tri}')
           