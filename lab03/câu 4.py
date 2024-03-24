n= int(input("nhap so nguyen duong n:"))
for i in range(n,0,-1):
    for j in range(2,1):
        if i%j == 0:
            break
        else:
            print("so nguyen to la:",i)
            break