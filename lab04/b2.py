import math
n = int((input("Nhập số nguyên dương n: ")))
tong_a = sum((-1) ** (i + 1) / i for i in range(1, n + 1))
tong_b = sum(1 / (i * (i + 1)) for i in range(1, n + 1))
tong_c = sum(1 / math.sqrt(i) for i in range(2, n + 2))
print("a. S =", tong_a)
print("b. S =", tong_b)
print("c. S =", tong_c)