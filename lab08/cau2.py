def tim_ucln(a, b):
    while b:
        a, b = b, a % b
    return a
# tìm phân số rút gọn
def rut_gon(tu_so,mau_so):
    ucln=tim_ucln(tu_so,mau_so)
    tu_so_rut_gon=tu_so//ucln
    mau_so_rut_gon=mau_so//ucln 
    return tu_so_rut_gon,mau_so_rut_gon
tu_so=int(input('nhập vào tử sổ:'))
mau_so=int(input('nhập vào mẫu số:'))
tu_so_rut_gon,mau_so_rut_gon=rut_gon(tu_so,mau_so) 
print(tu_so_rut_gon,"/",mau_so_rut_gon) 