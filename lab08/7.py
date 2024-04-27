def so_lon_nhat(a, b, c):
    return max(a, b, c)
def so_nho_nhat(a, b, c):
    return min(a, b, c)
a=int(input("Nhập số nguyên thứ nhất: "))
b=int(input("Nhập số nguyên thứ hai: "))
c=int(input("Nhập số nguyên thứ ba: "))
lon_nhat=so_lon_nhat(a, b, c)
nho_nhat=so_nho_nhat(a, b, c)
print("Số lớn nhất là: ", lon_nhat)
print("Số nhỏ nhất là: ", nho_nhat)