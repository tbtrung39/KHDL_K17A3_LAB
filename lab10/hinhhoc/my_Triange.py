def dien_tich_tam_giac(a, b, c):
    "Tinh dien tich tam giac theo cong thuc Heron"
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
def chu_vi_tam_giac(a, b, c):
    "Tinh chu vi tam giac"
    return a+b+c
    
