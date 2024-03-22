n=int(input("Nhap so nguyen n: "))
tong=0
for i in range(1, n+1):
    tong+=i**3
print("Tong bac ba cua", n, "so nguyen dau tien la:", tong)