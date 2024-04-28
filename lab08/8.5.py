def tim_ucln(a, b):
    while b:
        a, b = b, a % b
    return a

so_a = int(input("Nhập số a: "))
so_b = int(input("Nhập số b: "))

ucln = tim_ucln(so_a, so_b)
print("Ước chung lớn nhất của", so_a, "và", so_b, "là:", ucln)