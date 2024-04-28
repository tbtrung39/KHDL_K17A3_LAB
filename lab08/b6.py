def UCLN(a,b):
    if a < b:
        a, b = b, a
    while b != 0:
        so_du = a % b
        a = b
        b = so_du
    return a

def BCNN(a,b):
    ucln= UCLN(a,b)
    bcnn = (a*b)//ucln
    return bcnn
a = int(input("nhập số a: "))
b = int(input("nhập số b: "))
bcnn = BCNN(a,b)
print(f"bội chung nhỏ nhất của{a} và {b} là: {bcnn}")