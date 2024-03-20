#S5 = 1^3 + 3^3 + 5^3 +...+ (2n+1)^3
n = int(input("Nhập vào n: "))
tong = 1
if n<=0:
    print(n,"không phải là số nguyên dương, vui lòng nhập lại")
else:
    for i in range(1, n+1):
        tong +=(2*i+1)**3
        i+=1
print("Tổng của dãy số S5 là:",tong)        