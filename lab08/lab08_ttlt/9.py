def n(a,b):
    return (a+b), (a-b),(a*b),(a%b)
a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))
x = n(a,b)
print(f"Cong, tru , nhan ,chia cua {a} va {b} lan luot la: {n(a,b)}")
