#Viết chương trình nhập n là số nguyên dương. Nếu n<=0 dừng chương trình. Sau đó tính các tổng sau:

#a) S1 = 1 + 2 + 3 + … + n
#b) S2 = 1 + 3 + 5 + … + (2n+1)
#c) S3 = 2 + 4 + 6 + … + 2n
#a
n = int(input('nhập vào số nguyên n :'))
s=0
i=1
for i in range (1,n+1):
    s+=i
if n <=0:
   print('dừng')
print(s)
#b
n = int(input('nhập vào số nguyên n :'))
s=1
i=1
for i in range (1,n+1):
    s+=2**n+1
if n <=0:
   print('dừng')
print(s)
#c
n = int(input('nhập vào số nguyên n :'))
s=0
i=1
for i in range (1,n+1):
    s+=2*n
if n <=0:
   print('dừng')
print(s)