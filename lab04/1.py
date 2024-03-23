n=int(input("nhap so nguyen duong n: "))
while n<=0:
    n=int(input("khong phai so nguyen duong, vui long nhap lai: "))
S4=0
i=1
while i <= n:
    S4+=i**2
    i+=1

S5=0
i=1
while i <= n:
    S5+=i**3
    i+=2  

S6=0
i=2
while i<= n:
    S6+= i**4
    i += 2

print("Tổng S4=", S4)
print("Tổng S5=", S5)
print("Tổng S6=", S6)
