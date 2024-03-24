n= int(input("nhap n so nguyen to dau tien:"))
tong = 0
for i in range(1,n+1):
     tong += i/n
print(f"tong nghich dao cua {n} so nguyen to dau tien la:{tong}")