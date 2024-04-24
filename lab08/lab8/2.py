def ucln(a, b):
    while(b):
        a, b = b, a % b
    return a

def rut_gon_phan_so(tu, mau):
    ucln_val = ucln(tu, mau)
    tu = tu // ucln_val
    mau = mau // ucln_val
    return tu, mau

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
tu, mau = rut_gon_phan_so(tu, mau)
print("Phân số sau khi rút gọn là {}/{}".format(tu, mau))
