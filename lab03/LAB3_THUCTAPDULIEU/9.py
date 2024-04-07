#tinh tong 
# S4= 1**2 + 2**2 + 3**2 + ...+ n**2
# S5= 1**3 + 3**3 + 5**3 +...+ (2n+1)**3
# S6 =2**4 + 4**4 + 6**4 +...+ (2n)*4
n =int(input('Nhap so nguyen duong n:'))
if n<=0:
    print("n phai la so duong.Chuong trinh dung lai")
else:
    S4 = 0
    S5 = 0
    S6 = 0
for i in range(1 , n+1):
    S4 += i**2
    S5 += (2*i+1)**3
    S6 += (2*n)**4
print ('S4 =',S4)  
print ('S5 =', S5)
print ('S6 = ', S6)  
   
        