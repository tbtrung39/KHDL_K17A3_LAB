def tim_so_lon_nhat(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
def nhap_ba_so():
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    c = float(input("Nhập số thứ ba: "))
    return a, b, c
a, b, c = nhap_ba_so()
so_lon_nhat = tim_so_lon_nhat(a, b, c)
print(f"Số lớn nhất trong ba số {a}, {b}, {c} là: {so_lon_nhat}")
