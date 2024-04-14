n = int(input("Nhập số n: "))
A = [[int(i == j) for j in range(n)] for i in range(n)]
print("Ma trận đơn vị bậc", n, ":")
for row in A:
    print(row)