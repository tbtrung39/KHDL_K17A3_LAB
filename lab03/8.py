#cau a
n = int(input("Nhập số n: "))
if n <= 0:
    print("Số n không hợp lệ")
else:
    S1 = 0
    for i in range(1, n+1):
        S1 += i
    print("Tổng S1 =", S1)


#cau b
n = int(input("Nhập số n: "))
if n <= 0:
    print("Số n không hợp lệ")
else:
    S2 = 0
    for i in range(n+1):
        S2 += 2*i + 1
    print("Tổng S2 =", S2)


#cau c
n = int(input("Nhập số n: "))
if n <= 0:
    print("Số n không hợp lệ")
else:
    S3 = 0
    for i in range(1, n+1):
        S3 += 2*i
    print("Tổng S3 =", S3)


