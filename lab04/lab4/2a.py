n=int(input("nhap mot so:"))
tong_a=0
for i in range(1,n+1):
    tong_a+=(-1)**(i+1)*1/i
print("tong cua day so a la :",tong_a)