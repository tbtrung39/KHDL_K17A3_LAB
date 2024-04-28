def uoc_chung_lon_nhat(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        phan_du = a % b
        a = b
        b = phan_du
    return a

def boi_chung_nho_nhat_1(a,b):
    ucln = uoc_chung_lon_nhat(a, b)
    bcnn = (a * b) // ucln
    return bcnn
# Chương trình chính
a, b = map(int, input("Nhập giá trị của a và b, cách nhau bởi dấu cách: ").split())
bcnn = boi_chung_nho_nhat_1(a,b)
print("BCNN của 2 số", a, "và", b, "là:", bcnn)
