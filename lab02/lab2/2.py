a = int(input("nhap a:"))
b = int(input("nhap b:"))
c = int(input("nhap c:"))
import math
delta = b**2 - 4*a*c
if delta < 0:
    print("phuong trinh vo nghiem:")
elif delta == 0:
    x1 = -b/2*a
    print("phuong trinh co nghiem kep :",x1)
else  :
    x1 = (-b + (math.sqrt(b**2-4*a*c))/2*a)
    x2 = (-b - (math.sqrt(b**2-4*a*c))/2*a)
    print(f"phuong trinh co 2 nghiem :{x1},{x2}")
