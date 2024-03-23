import math
x=float(input("nhap ban kinh :"))
y=float(input("nhap chieu cao :"))
pi = 3.14
dien_tich_xung_quanh = 2*pi*x*y
dien_tich_xung_quanh=round(dien_tich_xung_quanh,2)
dien_tich_toan_phan = dien_tich_xung_quanh + 2*pi*x**2
dien_tich_toan_phan=round(dien_tich_toan_phan,2)
the_tich_khoi_tru=pi*x**2*y
the_tich_khoi_tru=round(the_tich_khoi_tru,2)
print("dien tich xung quanh cua hinh tru la :",dien_tich_xung_quanh)
print("dien tich toan phan la :",dien_tich_toan_phan)
print("the tich khoi tru la :",the_tich_khoi_tru)