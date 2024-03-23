n=int(input("nhap mot so:"))
tong_b=0
for i in range(1,n+1):
    tong_b+=1/(i*(i+1))
print("tong cua day so b la :",tong_b)