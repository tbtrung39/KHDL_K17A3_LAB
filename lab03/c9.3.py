#cau a
n = int(input("Nhập số n: "))
if n <= 0:
    print("Số n không hợp lệ")
else:
    S4 = 0
    for i in range(1, n+1):
        S4 += i**2
    print("Tổng S4 =", S4)


#cau b
n = int(input("Nhập số n: "))
if n <= 0:
    print("Số n không hợp lệ")
else:
    S5 = 0
    for i in range(0, n+1):
        S5 += (2*i + 1)**3
    print("Tổng S5 =", S5)


#cau c
n = int(input("Nhập số n: "))
if n <= 0:
    print("Số n không hợp lệ")
else:
    S6 = 0
    for i in range(1, n+1):
        S6 += (2*i)**4
    print("Tổng S6 =", S6)