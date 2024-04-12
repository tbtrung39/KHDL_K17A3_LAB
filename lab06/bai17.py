n = int(input("Nhập số n: "))

# Tạo ma trận đơn vị bậc n
A = [[int(i == j) for j in range(n)] for i in range(n)]

# In ma trận đơn vị
print("Ma trận đơn vị bậc", n, ":")
for row in A:
    print(row)