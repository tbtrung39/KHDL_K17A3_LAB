#a
n = int(input("Nhập vào số nguyên dương n: "))
tong = 0
i = 1
while n<1:
    n=int(input("vui lòng nhập lại: "))
while i<=n:
    tong +=i**2
    i+=1
print("Tổng của dãy số S4 là: ",tong)    

#b
n = int(input("Nhập vào số nguyên dương n: "))
tong = 0
i = 0
while n <0:
    n = int(input("vui lòng nhập lại: "))
while i<=n:
    tong +=(2*i+1)**3
    i+=1
print("Tổng của dãy số S5 là: ",tong)    

#c
n = int(input("Nhập số nguyên dương n: "))
tong = 0
i = 1
while n<0:
    n=int(input("vui lòng nhập lại: "))
while i<=n:
    tong += (2*i)**4
    i+=1
print("Tổng của dãy số S6 là: ",tong)        