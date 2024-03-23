n = int(input("nhap mot so:"))
hoan_hao = []
for i in range(2,n):
    s=0
    for j in range(1,n):
        if i%j == 0:
            s+=1
    if s == i:
        hoan_hao.append(i)
        print(f"cac so hoan hao nho hon",n,"la:")
        for so in hoan_hao:
            print(so)