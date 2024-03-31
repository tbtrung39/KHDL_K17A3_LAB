#Viết chương trình nhập n là số nguyên dương. Nếu n<=0 thì dừng chương trình. Sau đó tính các tổng sau bằng vòng lặp for:

#a) S4 = 1^2 + 2^2 + 3^2 + … + n^2.
#b) S5 = 1^3 + 3^3 + 5^3 + … + (2n+1)^3.
#c) S6 = 2^4 + 4^4 + 6^4 + … + (2n)^4.

#a
n = int(input('nhập vào số nguyên n :'))
s=0
i=1
for i in range (1,n+1):
    s+=i**2
if n <=0:
   print('dừng')
print(s)
#b
n = int(input('nhập vào số nguyên n :'))
s=1
i=1
for i in range (1,n+1):
    s+=(2*n+1)**3
if n <=0:
   print('dừng')
print(s)
#c
n = int(input('nhập vào số nguyên n :'))
s=0
i=1
for i in range (1,n+1):
    s+=(2*n)**4
if n <=0:
   print('dừng')
print(s)