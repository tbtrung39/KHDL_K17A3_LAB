#Giai phuong trinh ax^2 + bx + c = 0
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
x = 0
if a == 0:
    x = -c/b
    print("Phương trình có 1 nghiệp duy nhất: ",x)
else:
    delta = b**2 - (4*a*c)    
    if delta > 0:
        x1 = (-b + (delta)**0.5)/2*a
        x2 = (-b - (delta)**0.5)/2*a
        print("Phương trình có 2 nghiệm phân biệt x1 = ",x1 ,"và x2 = ",x2)
    elif delta == 0:
        x = -b/(2*a)
        print("Phương trình có nghiệm kép x = ",x)
    else:
        print("Phương trình vô nghiệm")