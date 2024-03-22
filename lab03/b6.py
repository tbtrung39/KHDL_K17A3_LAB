n = int(input("Nhập số nguyên dương n: "))
total = sum([i ** 3 for i in range(1, n + 1)])
print("Tổng bậc 3 của", n, "số nguyên đầu tiên là:", total)