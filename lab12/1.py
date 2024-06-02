import math
def nhap_so_thuc (thong_bao):
    try:
        gia_tri=float (input (thong_bao))
        if gia_tri<=0:
            raise ValueError ("Gia tri lon hon 0")
        return gia_tri
    except ValueError as ve:
        print(f" Loi: (ve)")
        return None
def la_tam_giac_hop_le(a, b, c):
    return a+b>c and a+c>b and b+c>a
def tinh_dien_tich_tam_giac(a, b, c):
    nua_chu_vi=(a+b+c)/2
    return math.sqrt(nua_chu_vi*(nua_chu_vi-a) * (nua_chu_vi-b)*(nua_chu_vi-c))
def chay_chuong_trinh():
    a=nhap_so_thuc ("Nhap do dai canh a: ")
    if a is None: return 
    b=nhap_so_thuc("Nhap do dai canh b: ")
    if b is None: return
    c=nhap_so_thuc ("Nhap do dai canh c: ")
    if c is None: return 
    if not la_tam_giac_hop_le(a, b, c):
        print("Loi: Ba canh a, b, c khong thoa man dieu kien ton tai tam giac")
        return
    dien_tich=tinh_dien_tich_tam_giac(a, b, c)
    print(f"Dien tich tam giac la: {dien_tich}")
chay_chuong_trinh()