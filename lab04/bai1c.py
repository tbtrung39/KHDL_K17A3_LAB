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