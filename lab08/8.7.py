def so_nho_nhat(a, b, c):
    return min(a, b, c)

def so_lon_nhat(a, b, c):
    return max(a, b, c)

so_1 = int(input("Nhập số thứ nhất: "))
so_2 = int(input("Nhập số thứ hai: "))
so_3 = int(input("Nhập số thứ ba: "))

min_so = so_nho_nhat(so_1, so_2, so_3)
max_so = so_lon_nhat(so_1, so_2, so_3)

print("Số nhỏ nhất là:", min_so)
print("Số lớn nhất là:", max_so)