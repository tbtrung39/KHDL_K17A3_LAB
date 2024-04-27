def phep_tinh(a, b):
    return a+b, a-b, a*b, a/b
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
tong, hieu, tich, thuong = phep_tinh(a,b)
print("Tổng của hai số",a,"và",b,"là:",tong)
print("Hiệu của hai số",a,"và",b,"là:",hieu)
print("Tích của hai số",a,"và",b,"là:",tich)
print("Thương của hai số",a,"và",b,"là:",thuong)
