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