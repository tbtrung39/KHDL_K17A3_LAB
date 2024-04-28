def tim_bcnn(a, b):
    bcnn = (a * b) // tim_ucln(a, b)
    return bcnn

def tim_ucln(a, b):
    while b:
        a, b = b, a % b
    return a

so_a = int(input("Nhập số a: "))
so_b = int(input("Nhập số b: "))

bcnn = tim_bcnn(so_a, so_b)
print("Bội chung nhỏ nhất của", so_a, "và", so_b, "là:", bcnn)