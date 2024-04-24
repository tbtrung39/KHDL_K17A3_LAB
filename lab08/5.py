def UCLN(a,b):
    if a < b:
        a,b=b,a
    while b != 0:
        so_du = a % b
        a = b
        b = so_du
    return a

a = int(input("nhập số a: "))
b = int(input("nhập số b: "))
ucln = UCLN(a,b)
print(f"ước chung lớn nhất của {a} và {b} là: {ucln}")