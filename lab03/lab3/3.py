n = int(input("nhập số nguyên dương n: "))
for i in range(n,0,-1):
    for j in range(2,i):
        if i%j ==0:
            break
    else:
        print(f"số nto là gần {n} là: ",i)
        break 