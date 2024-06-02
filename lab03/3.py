n=int(input("Nhập số nguyên dương n: "))
for i in range(n,0,-1):
    for j in range(2,i):
        if i %j==0:
            break
    else:
        print("Số nguyên tố là :",i)
        break