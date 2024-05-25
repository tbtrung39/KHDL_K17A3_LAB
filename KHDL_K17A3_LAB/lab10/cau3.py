import package1.so_hoc as t
a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
print(f"UCLN của {a} và {b} là: ",t.Ucln(a,b))
print(f"BCNN của {a} và {b} là: ",t.Bcnn(a,b))

n=int(input("Nhập n: "))
print(f"Tổng các ước của {n} là: ",t.Sum_Divisor(n))