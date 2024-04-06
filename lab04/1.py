n = int(input("nhap so n:"))
while True:   
    if n <= 0:
        print("Vui lòng nhập lại số nguyên dương.")
    else:
        break

S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1
print("tong S4 = ", S4) 



n = int(input("Nhập một số nguyên dương n: "))
while True:
    if n <= 0:
        print("Vui lòng nhập lại số nguyên dương.")
    else:
        break
S5 = 0
i = 0
while i <= n:
    S5 += (2 * i + 1) ** 3
    i += 1
print("Tổng S5 =", S5)



n = int(input("Nhập một số nguyên dương n: "))
while True:
    if n <= 0:
        print("Vui lòng nhập lại số nguyên dương.")
    else:
        break
S6 = 0
i = 1
while i <= n:
    S6 += (2 * i) ** 4
    i += 1
print("Tổng S6 =", S6)

