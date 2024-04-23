n = int(input("Nhập số phần tử: "))
A = set()
for i in range(n):
    phan_tu = float(input("Nhập giá trị: "))
    A.add(phan_tu)
print(A)
gia_tri_max = max(A)
print("Giá trị lớn nhất của A là: ", gia_tri_max)
gia_tri_min = min(A)
print("Giá trị nhỏ nhất của A là: ", gia_tri_min)
tong = 0
for i in A:
    tong += i
print("Tổng các phần tử của tập hợp A là: ", tong)
