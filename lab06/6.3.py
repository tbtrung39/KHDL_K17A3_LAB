a =[]
while True:
    n = int(input("Nhập giá trị list(Nhập '0' để dừng): "))
    if n == 0:
        break
    a.append(n)
print(f'Danh sách list là: {a}')
#
a1=[i for i in a if i>0]
a2=[i for i in a if i<0]
a=a1+a2
#
so_moi = int(input('Chèn một số nguyên mới: '))
vtri = int(input('Nhập vào vị trí muốn thêm ( 1 - đầu, 2- giữa, 3- cuối): '))
if vtri == 1:
    a.insert(0,so_moi)
elif vtri == 2:
    a.insert(len(a)//2, so_moi)
else:
    a.append(so_moi)
print(f'Danh sách sau khi thêm là: {a}')