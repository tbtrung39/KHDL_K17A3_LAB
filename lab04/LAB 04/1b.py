n= int(input("Nhap so: "))
i=1
S5=0
while n<=0:
    n = int(input("Nhap lai so nguyen duong: "))
while i <= (2*n +1):
    S5 +=i**3
    i += 2
print("Tong S5 =" ,S5)
                   