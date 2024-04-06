#S4 =1^2 + 2^2 + ... + n^2
n = int(input("Nhập vào số nguyên dương n: "))
tong = 0
i = 1
while n<1:
    n=int(input("Giá trị không hợp lệ, vui lòng nhập lại: "))
while i<=n:
    tong +=i**2
    i+=1
print("Tổng của dãy số S4 là: ",tong)
#S5 = 1^3 + 3^3 +...+ (2n+1)^3
n = int(input("Nhập vào số nguyên dương n: "))
tong = 0
i = 0
while n <0:
    n = int(input("Giá trị không hợp lệ, vui lòng nhập lại: "))
while i<=n:
    tong +=(2*i+1)**3
    i+=1
print("Tổng của dãy số S5 là: ",tong)
#S6 = 2^4 + 4^4 +...+(2n)^4
n = int(input("Nhập số nguyên dương n: "))
tong = 0
i = 1
while n<0:
    n=int(input("Giá trị không hợp lệ, vui lòng nhập lại: "))
while i<=n:
    tong += (2*i)**4
    i+=1
print("Tổng của dãy số S6 là: ",tong)        