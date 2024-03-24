n=int(input("Nhap n:"))
# In ra cac so nguyen to tu tu 2 den n
dem_so_nguyen_to = 0
for i in range(2, n+1):
    la_so_nguyen_to=True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            la_so_nguyen_to=False
            break
    if la_so_nguyen_to:
        print(i,end=',')
        dem_so_nguyen_to += 1
        if dem_so_nguyen_to % 15 ==0:
            print()