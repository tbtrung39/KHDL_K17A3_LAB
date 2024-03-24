n = int(input('Nhap so nguyen duong n: '))
if n<= 0:
    print("n phai la so duong. Chuong trinh dung lai ")
else:
    S1 = 0
for i in range (1, n+1):
    S1  += i
print ("S1 = ", S1)            
