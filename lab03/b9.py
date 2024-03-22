n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Số n phải là số nguyên dương. Dừng chương trình.")
else:
    S4 = 0
    for i in range(1, n + 1):
        S4 += i ** 2
    S5 = 0
    for i in range(1, 2 * n + 2, 2):
        S5 += i ** 3
    S6 = 0
    for i in range(2, 2 * n + 1, 2):
        S6 += i ** 4
    print("a) Tổng S4 =", S4)
    print("b) Tổng S5 =", S5)
    print("c) Tổng S6 =", S6)