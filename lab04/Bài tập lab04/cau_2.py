# Câu a
tong = 0
n = int(input("Nhập n: "))
for i in range(1, n + 1):
    tong += 1/i
print("Tổng của dãy số là: ",tong)

# Câu b
tong = 0
n = int(input("Nhập n:"))
for i in range(n + 1):
    tong += 1/(n * n +1)
print("Tổng của dãy số là: ",tong)

# Câu c
import math
tong = 0
n = int(input("Nhập n:"))
for i in range(2, n + 1):
    tong += 1/math.sqrt(i)
print("Tổng của dãy số là: ",tong)