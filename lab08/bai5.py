def ucln(a, b):
    while b !=0:
        a, b = b, a%b
    return a
a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
uoc_chung = ucln(a,b)
print("Ước chung lớn nhất của hai số",a,"và",b,"là:",uoc_chung)