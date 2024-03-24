n = int(input("Nhập vào một số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    S1 = sum(i for i in range(1, n+1))
    S2 = sum(i for i in range(1, 2*n+2, 2))
    S3 = sum(i for i in range(2, 2*n+1, 2))
    print("S1 =", S1)
    print("S2 =", S2)
    print("S3 =", S3)