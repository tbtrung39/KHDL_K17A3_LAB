def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon_phan_so(tu_so, mau_so):
    ucln = tim_ucln(tu_so, mau_so)
    tu_so_rut_gon = tu_so // ucln
    mau_so_rut_gon = mau_so // ucln
    return tu_so_rut_gon, mau_so_rut_gon

try:
    tu_so = int(input("Nhập tử số của phân số: "))
    mau_so = int(input("Nhập mẫu số của phân số: "))

    if mau_so == 0:
        print("Mẫu số phải khác 0.")
    else:
        tu_so_rut_gon, mau_so_rut_gon = rut_gon_phan_so(tu_so, mau_so)
        print(f"Phân số sau khi rút gọn là: {tu_so_rut_gon}/{mau_so_rut_gon}")
except ValueError:
    print("Vui lòng chỉ nhập số nguyên.")
