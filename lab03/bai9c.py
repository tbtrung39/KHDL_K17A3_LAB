#S6 = 2^4 + 4^4 + 6^4 +... + (2n)^4
n = int(input("Nhập vào n: "))
tong = 0
if n<=0:
    print(n,"không phải là số nguyên dương, vui lòng nhập lại")
else:
    for i in range(1, n+1):
        tong += (2*i)**4
        i+=1
print("Tổng của dãy số S6 là:",tong)        