n = int(input("Nhập số nguyên dương n: "))
S = 0
i = 1
dau = 1
while n<=0:
 n= int(input('nhap lai so nguyen duong: '))
while i <= n:
    S += dau * 1 / i
    dau *= -1
    i += 1

print("Tổng của dãy số S là:", S)