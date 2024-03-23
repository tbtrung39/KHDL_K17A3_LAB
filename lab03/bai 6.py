
n=int(input("Nhap so nguyen duong a:"))
gia_tri_ban_dau=0
for i in range(1, n+1):
    gia_tri_ban_dau += i**3
print("Tong bac ba cua",n,"so nguyen dau tien la:",gia_tri_ban_dau)
