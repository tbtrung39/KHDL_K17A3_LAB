n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Số bạn nhập không phải là số nguyên dương. Vui lòng nhập lại n: "))

# Tính tổng S4
s4 = 0
i = 0
while i <= n:
    s4 += i ** 2
    i += 1

# Tính tổng S5
s5 = 0
i = 0
while i <= n-1:
    s5 += (2 * i + 1) ** 3
    i += 1

# Tính tổng S6
s6 = 0
i = 0
while i <= 2 * n:
    s6 += i ** 4
    i += 2

print("Tổng S4:", s4)
print("Tổng S5:", s5)
print("Tổng S6:", s6)
