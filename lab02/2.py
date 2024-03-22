a=int(input("Nhap vao gia tri a: "))
b=int(input("Nhap vao gia tri b: "))
c=int(input("Nhap vao gia tri c: "))
delta=b**2-4*a*c
if delta>0:
    x1=(-b+delta**0.5)/2*a
    x2=(-b-delta**0.5)/2*a
    print(f"Phuong trinh co 2 nghiem phan biet: x1={x1} va x2={x2}")
elif delta==0:
    x=-b/2*a
    print(f"Phuong trnh co 1 nghiem kep: x3={x3}")
else:
    print("Phuong trnh vo nghiem")