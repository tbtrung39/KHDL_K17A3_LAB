import my_Triange
a=float(input("Nhap canh a: "))
b=float(input("Nhap canh b: "))
c=float(input("Nhap canh c: "))
if my_Triange.is_TamGiac(a, b, c):
    print("Ba canh nay tao thanh mot tam giac")
    chu_vi=my_Triange.ChuviTamgiac(a, b, c)
    print(f"Chu vi tam giac la: {chu_vi}")
    dien_tich=my_Triange.S_TamGiac(a, b, c)
    print(f"Dien tich tam giac la: {dien_tich}")
else:
    print("Ba canh nay khong tao thanh mot tam giac")

