def ucln(a,b):
    while b!=0:
        a,b = b,a%b
    return a
def phan_so(tu,mau):
    Ucln = ucln(tu,mau)
    rut_gon_tu = tu//Ucln
    rut_gon_mau = mau//Ucln
    return rut_gon_tu, rut_gon_mau
tu = int(input('Nhập vào tử: '))
mau = int(input('Nhập vào mẫu: '))
rut_gon_tu, rut_gon_mau =phan_so(tu,mau)
print(f'Phân số sau khi rút gọn là: {rut_gon_tu}/{rut_gon_mau}')