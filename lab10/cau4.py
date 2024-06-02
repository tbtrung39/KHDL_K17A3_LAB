import package1.pt as t
#Giải phương trình bậc nhất mx+n=0
print("NHẬP PHƯƠNG TRÌNH BẬC NHẤT mx + n = 0")
m=int(input("Nhập m: "))
n=int(input("Nhập n: "))
print(f"Nghiệm của phương trình bậc nhất {m}x + {n} = 0 là : {t.giai_phuong_trinh_bac_nhat(m,n)}")

#Giải phương trình bậc hai ax^2 + bx + c = 0
print("NHẬP PHƯƠNG TRÌNH BẬC HAI AX^2 + BX + C = 0")
a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
c=int(input("Nhập c: "))
print(f"Nghiệm của phương trình bậc hai {a}x^2 + {b}x + c = 0 là : {t.giai_phuong_trinh_bac_hai(a,b,c)}")