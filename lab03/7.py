n=int(input("Nhap so nguyen n: "))
if n<=0:
    print("Vui lòng nhập một số nguyên dương lớn hơn")
tong=0
for i in range(1, n+1):
    tong+=i 
print("Tong S1 =", tong)
 
tong=0
for i in range(1, n+1):
    tong+=2*i+1
print("Tong S2 =", tong)

tong=0
for i in range(2, n+1):
    tong+=2*i 
print("Tong S3 =", tong)