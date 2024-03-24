n =int(input("Nhap so nguyen duong n: "))
S3 = 0
i = 2

while n<=0:
    n = int(input("Nhap lai so nguyen duong n: "))
while i<=n :
    S3 += 1 / (i**0.5) 
    i += 1   

print("Tong day so cua S3 la:", S3)    