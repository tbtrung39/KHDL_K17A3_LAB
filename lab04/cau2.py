#a
n=int(input("nhap mot so:"))
tong_a=0
for i in range(1,n+1):
    tong_a+=(-1)**(i+1)*1/i
print("tong cua day so a la :",tong_a)

#b
n=int(input("nhap mot so:"))
tong_b=0
for i in range(1,n+1):
    tong_b+=1/(i*(i+1))
print("tong cua day so b la :",tong_b)

#c
import math
n=int(input("nhap mot so:"))
tong_c=0
for i in range(2,n+2):
    tong_c+=1/math.sqrt(i)
print("tong cua day so c la :",tong_c)