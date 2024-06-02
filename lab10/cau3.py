import package1.so_hoc as s
a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
print(f"UCLN của {a} và {b} là: ",s.Ucln(a,b))
print(f"BCNN của {a} và {b} là: ",s.Bcnn(a,b))

n=int(input("Nhập n: "))
print(f"Tổng các ước của {n} là: ",s.Sum_Divisor(n))