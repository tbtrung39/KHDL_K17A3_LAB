# tinh tong: S2= 1+3+5+...+(2n+1)
n = int(input("Nhap so nguyen duong n: "))
if n<=0:
    print("n phai la so duong. Chuong trinh dung lai")
else:
    S2 = 0
for i in range(1, n+1) :
    S2 += 2*i +1
print("S2 = ", S2)           