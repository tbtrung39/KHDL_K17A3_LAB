n=int(input("Nhap so nguyen duong n: "))
for i in range(n, 0, -1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print("So nguyen to la: ",i)
        break