a = float(input("nhap so a: "))
b = float(input("nhap so b: "))
c = float(input("nhap so c: "))
delta = b**2 - 4*a*c
if delta >0:
    x1 =(-b + math.sqrt(delta))/2*a 
    x2 =(-b - math.sqrt(delta))/2*a 
    print("phuong trinh co 2 nghiem phan biet")
    print("x1= ",x1)
    print("x2= ",x2)
elif delta ==0:
    x = -b/2*a
    print("phuong trinh co nghiem kep")
    print("x=",x)
else:
    print("phuong trinh vo nghiem")