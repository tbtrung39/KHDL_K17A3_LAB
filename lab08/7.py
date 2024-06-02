def tim_so_lon_nhat(a, b, c):
    return max(a, b, c)

def tim_so_nho_nhat(a, b, c):
    return min(a, b, c)

# Nhập 3 số nguyên từ bàn phím
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

# Tìm và in ra số lớn nhất và nhỏ nhất
so_lon_nhat = tim_so_lon_nhat(a, b, c)
so_nho_nhat = tim_so_nho_nhat(a, b, c)

print(f"Số lớn nhất là: {so_lon_nhat}")
print(f"Số nhỏ nhất là: {so_nho_nhat}")
