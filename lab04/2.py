n=int(input("Nhap so phan tu cua chuoi: "))
S1=0
for i in range (1, n+1):
    if i%2==0:
        S1 -= 1/i 
    else:
        S1 += 1/i

S2=0
for i in range(2, n+2):
    S2+=1/((i-1)*i)


S3=0
for i in range(2, n+2):
    S3+=1/(i**1/2)
print ("Tong cua chuoi la: ", S1)
print ("Tong cua chuoi la: ", S2)
print ("Tong cua chuoi la: ", S3)