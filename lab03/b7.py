n = int(input("Nhập số nguyên dương n: "))
total_inverse = 0
for i in range(1, n + 1):
    total_inverse += 1 / i
print("Tổng nghịch đảo của", n, "số nguyên đầu tiên là:", total_inverse)