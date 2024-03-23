r = float(input("Nhap ban kinh : "))
h = float(input("Nhap chieu cao: "))
pi = 3.14
dien_tich_xq = 2*pi*r*h
dien_tich_xq = round(dien_tich_xq, 2)
dien_tich_tp = dien_tich_xq + 2*pi*r**2
dien_tich_tp = round(dien_tich_tp, 2)
the_tich = pi*r**2*h
the_tich = round(the_tich, 2)
print(dien_tich_xq)
print(dien_tich_tp)
print(the_tich)