def tim_ucln(a,b):
    while b:
        a,b = b, a%b
    return a

def rut_gon_phan_so(tu_so,mau_so):
    ucln = tim_ucln(tu_so, mau_so)
    tu_so_rut_gon = tu_so// ucln
    mau_so_rut_gon = mau_so//ucln
    return tu_so_rut_gon,mau_so_rut_gon
tu_so = int(input("nhap tu so :"))
mau_so = int(input("nhap mau so :"))
tu_so_rut_gon,mau_so_rut_gon = rut_gon_phan_so(tu_so,mau_so)
print("phan so sau khi duoc rut gon la:",tu_so_rut_gon,"/",mau_so_rut_gon)