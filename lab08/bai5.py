def ucln(a, b):
    while b !=0:
        a, b = b, a%b
    return a
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
uoc_chung = ucln(a,b)
print("Ước chung lớn nhất của hai số",a,"và",b,"là:",uoc_chung)