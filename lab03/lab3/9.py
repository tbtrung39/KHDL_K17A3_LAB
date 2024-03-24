n = int(input("Nhập vào một số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    S4 = sum(i**2 for i in range(1, n+1))
    S5 = sum(i**3 for i in range(1, 2*n+2, 2))
    S6 = sum(i**4 for i in range(2, 2*n+1, 2))
    print("S4 =", S4)
    print("S5 =", S5)
    print("S6 =", S6)