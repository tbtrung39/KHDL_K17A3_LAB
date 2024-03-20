a = float(input("nhap so nguyen a :"))
b = float(input("nhap so nguyen b :"))
c = float(input("nhap so nguyen c :"))
delta = ((b**2 - 4*a*c))
if delta >0:
    x1= (-b+delta**0.5)/2
    x2= (-b-delta**0.5)/2
    print("phuong trinh co 2 nghiem phan biet",x1,x2)
elif delta == 0:
    x= (-b/2*a)
    print("phuong trinh co nghiem duy nhat",x)
else:
    print("phuong trinh vo nghiem")