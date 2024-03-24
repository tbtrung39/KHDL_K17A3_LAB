n = int(input("Nhập vào một số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    S = 1
    for i in range(1, n+1):
        term = 2*(i+1) / (2*i + 3)
        if (i+1) % 2 == 0:
            S -= term
        else:
            S += term
    S = round(S, 3)
    print("Kết quả của phép toán là:", S)