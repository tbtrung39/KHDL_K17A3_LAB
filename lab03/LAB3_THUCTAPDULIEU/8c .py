# Tinh tong S3 = 2+4+6+...+2n

n = int(input('Nhap so nguyen duong n: '))
if n <=0:
    print("n phai la so nguyen duong.Chuong trinh dung lai")
else:
    S3 =0
for i in range(1, n+1) :
    S3 += 2*i
print('S3 =', S3)           