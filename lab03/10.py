so_hang= int(input("nhap so hang cua tam giac:"))
ve_tam_giac= 0
for i in range(so_hang):
    for j in range(so_hang-i-1):
        print(" ",end="")
    for j in range(i*2+1):
        if j==0 or j== i*2 or i==so_hang-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()