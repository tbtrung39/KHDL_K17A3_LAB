n = int(input("Nhập số n: "))
a = 0
for i in range(1, n+1):
    a += 1 / i
print("Tổng nghịch đảo của", n, "số nguyên đầu tiên là:", a)