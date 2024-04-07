n= int(input("Nhap so: "))
i=1
S6=0
while n<=0:
    n = int(input("Nhap lai so nguyen duong: "))
while i <= (2*n):
    S6 +=i**4
    i += 3
print("Tong S6 =" ,S6)
                   