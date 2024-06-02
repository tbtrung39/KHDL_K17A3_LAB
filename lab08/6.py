def ucln(a, b):
    while(b != 0):
        a, b = b, a % b
    return a

def bcnn(a, b):
    return abs(a*b) // ucln(a, b)

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print(f"BCNN của {a} và {b} là: {bcnn(a, b)}")
