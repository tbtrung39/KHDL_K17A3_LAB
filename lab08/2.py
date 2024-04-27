def tim_ucln(a, b):
    while b!=0:
        a, b=b, a%b
    return a
def rut_gon_phan_so(tu_so, mau_so):
    ucln=tim_ucln(tu_so, mau_so)
    tu_so_rut_gon=tu_so//ucln
    mau_so_rut_gon=mau_so//ucln
    return tu_so_rut_gon, mau_so_rut_gon
tu_so=int(input("Nhập tử số: "))
mau_so=int(input("Nhập mẫu số: "))
tu_so_rut_gon, mau_so_rut_gon = rut_gon_phan_so(tu_so, mau_so)
print("Phân số sau khi được rút gọn là: ", tu_so_rut_gon, "/", mau_so_rut_gon)
