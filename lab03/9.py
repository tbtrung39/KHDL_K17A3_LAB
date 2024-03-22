n=int(input("Nhap so nguyen duong: "))
for i in range(2, n+1):
    tong=0
    while n%i==0:
        n//=i 
        tong+=i 
    if tong>0:
        print(i, "^", tong, end=" ")