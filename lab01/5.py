
import math

xA,yA=map(int,input("Nhap vector a :").split())
xB,yB=map(int,input("Nhap vector b :").split())
x=math.sqrt(xA**2+yA**2)
y=math.sqrt(xB**2+yB**2)
cosx_y=(xA*xB+yA*yB)/x*y
tich_vo_huong=x*y*cosx_y
print("Tich vo huong cua 2 vecto do la :",tich_vo_huong)
