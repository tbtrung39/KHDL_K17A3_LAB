
n = int(input("Nhập số thuật ngữ (n): "))

tong = 0  

for k in range(n+1):
    term = 1
    for i in range(1, 2*k+2):
        term *= (2*i)/(2*i - 1)
    tong += term

lam_tron_tong = round(tong, 3)

print(f"Tổng của biểu thức cho n={n} là: {lam_tron_tong}")


