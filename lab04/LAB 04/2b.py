n = int(input("Nhap so nguyen duong n: "))
S2 = 0
i =1

while n<=0:
    n = int(input("Nhap lai so nguyen duong n: "))
while i<=n:
    S2 += 1/(i*(i+1))
    i += 1
print("Tong day cua S2 la:" , S2)        
