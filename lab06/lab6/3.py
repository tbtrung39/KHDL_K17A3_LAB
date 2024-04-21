danh_sach = []
while True:
    n = int(input("Nhap mot so tu nhien (0 de ket thuc nhap) la:"))
    if n == 0:
        break
    danh_sach.append(n)
print(danh_sach)

a = sorted(danh_sach,reverse=True)
print("Danh sach sau khi chuyen so duong len dau la:",a)
m = int(input("Nhap m la:"))
danh_sach.append(m)
danh_sach.insert(0,m)
danh_sach.insert(4,m)
print("Danh sach sau khi chen so m la:",danh_sach)