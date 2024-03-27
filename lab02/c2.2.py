a = int(input("Nhap vao a:"))
b = int(input("Nhap vao b:"))
c = int(input("Nhap vao c:"))
delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + delta**0.5)/2
    x2 = (-b + delta**0.5)/2
    print("Phuong trinh co 2 nghiem phan biet")
elif delta == 0:
    print("Phuong trinh co nghiem duy nhat")
else:
    print("Phuong trinh vo nghiem")