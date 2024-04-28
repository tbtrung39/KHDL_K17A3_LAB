def uoc_chung_lon_nhat(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        phan_du = a % b
        a = b
        b = phan_du
    return a

# Chương trình chính
a, b = map(int, input("Nhập giá trị của a và b, cách nhau bởi dấu cách: ").split())
ucln = uoc_chung_lon_nhat(a, b)
print("ƯCLN của", a, "và", b, "là:", ucln)
