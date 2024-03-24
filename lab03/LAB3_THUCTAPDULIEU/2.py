n = int(input("Nhap so nguyen duong n: "))
so_hoan_hao=[]
for j in range(2,n):
    tong=0
    for i in range(1,j):
        if j % i == 0:
            tong +=i
    if tong == j:
        so_hoan_hao.append(j)
print("Cac so hoan hao nho hon",n,"la:", so_hoan_hao)

                   