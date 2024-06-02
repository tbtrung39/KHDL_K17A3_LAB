def ucln(a, b):
    while(b != 0):
        a, b = b, a % b
    return a

def rut_gon_phan_so(a, b):
    ucln_ab = ucln(a, b)
    return a // ucln_ab, b // ucln_ab

tu_so=int(input("Nhập tử số: "))
mau_so=int(input("Nhập mẫu số: "))
tu_so,mau_so=rut_gon_phan_so(tu_so,mau_so)
print(f"Phân số sau khi rút gọn: {tu_so}/{mau_so}")
