n = int(input("Nhập số phần tử: "))
x = []
for i in range(n):
    phan_tu = int(input(f"Nhập các phần tử thứ {i + 1}: "))
    x.append(phan_tu)
print(x)
danh_sach_giam_dan = sorted(x, reverse=True)
phan_tu_2 = danh_sach_giam_dan[1]
vi_tri_2 = x.index(phan_tu_2)
print("Phần tử lớn thứ 2 của danh sách là: ", phan_tu_2)
print("Vị trí của phần tử lớn thứ 2 là: ", vi_tri_2)
# 
so_luong_max = 0
so_luong = 0
for i in x:
    if i > 0:
        so_luong += 1
        if so_luong > so_luong_max:
            so_luong_max = so_luong
    else:
        so_luong = 0
print("Số lượng phần tử dương liên tiếp nhiều nhất trong danh sách là:", so_luong_max)
# 
so_luong_max = 0
so_luong = 0
tong = 0
tong_max = 0
for i in x:
    if i > 0:
        tong += i
        so_luong += 1
        if tong > tong_max:
            tong_max = tong
            so_luong_max = so_luong
        elif tong ==tong_max:
            if so_luong > so_luong_max:
                so_luong_max = so_luong
    else:
        so_luong = 0
        tong = 0
print("Số lượng các số dương liên tiếp có tổng lớn nhất trong danh sách là: ",so_luong_max)
