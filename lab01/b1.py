import math
r = float(input("Nhap ban kinh khoi tru: "))
l = float(input("Nhap chieu cao khoi tru: "))
pi = 3.14
s_xq = 2 * pi * r * l
s_tp = 2 * pi *r * (r + l)
v = pi * r**2 * l
s_xq = round(s_xq, 2)
s_tp = round(s_tp, 2)
v = round(v, 2)
print("diện tích xung quanh khối trụ là: ",s_xq)
print("diện tích toàn phần khối trụ là: ",s_tp)
print("thể tích khối trụ là: ",v)