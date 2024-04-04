import math
x=float(input("nhap vao mot so:"))
tu_so = -x + (x**2)**(1/2)
mau_so = ((x**4)+1)**(1/7)
f = tu_so/mau_so
f = round(f,2)
print("gia tri cua f(x) la :",f)