import math
r=float(input("nhap ban kinh: "))
l=float(input("nhap chieu cao: "))
pi=3.14
s_xq = 2**pi*r*l
s_tp = s_xq + 2*pi*r**2
v_tru = pi*r**2*l
print("dien tich xung quanh la",s_xq)
print("dien tich toan phan la",s_tp)
print("the tich khoi tru la",v_tru)