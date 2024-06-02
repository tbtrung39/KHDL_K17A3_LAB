#a
n = int(input("Nhap vao mot so phan tu cua danh sach la : "))
danhsach = []

for i in range(n):
    phan_tu = int(input(f"Nhap vao phan tu thu la : {i+1}"))
    phan_tu += i
    danhsach.append(phan_tu)
print("danh sach cac phan tu la", danhsach)