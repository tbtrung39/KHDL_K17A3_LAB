n=int(input('nhap n: '))
for i in range(2,n):
    uc=[j for j in range(1,int(i/2+1)) if i%j==0]
    if sum(uc)==i:
        print(i,end=' ')