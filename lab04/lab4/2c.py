import math
n=int(input("nhap mot so:"))
tong_c=0
for i in range(2,n+2):
    tong_c+=1/math.sqrt(i)
print("tong cua day so c la :",tong_c)
