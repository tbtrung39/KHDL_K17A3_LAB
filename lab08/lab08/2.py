def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def rut_gon_phan_so(tu, mau):
    ucln = tim_ucln(tu, mau)
    tu_gon = tu // ucln
    mau_gon = mau // ucln
    return ucln, tu_gon, mau_gon
tu_so = int(input("Nhập tử số của phân số: "))
mau_so = int(input("Nhập mẫu số của phân số: "))
ucln, tu_gon, mau_gon = rut_gon_phan_so(tu_so, mau_so)
print("Ước chung lớn nhất của tử số và mẫu số là:", ucln)
print("Phân số sau khi được rút gọn là:", tu_gon, "/", mau_gon)
