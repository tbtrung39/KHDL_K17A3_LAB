def tim_ucln(a, b):
    while b!= 0:
        a, b=b, a%b
    return a
def tim_bcnn(a, b):
    ucln=tim_ucln(a, b)
    bcnn=(a*b)//ucln
    return bcnn
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
bcnn=tim_bcnn(a, b)
print("BCNN của", a, b, "là:", bcnn)