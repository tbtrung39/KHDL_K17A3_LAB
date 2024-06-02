# Nhập số hàng và số cột của ma trận
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

# Tạo ma trận A
A = []
for i in range(m):
 row = []
 for j in range(n):
   aij = int(input(f"Nhập phần tử a{i+1}{j+1}: "))
   row.append(aij)
 A.append(row)


# In ma trận A
print("Ma trận A:")
for row in A:
 print(row)
# Tính tổng các phần tử của ma trận A
total = 0
for i in range(m):
 for j in range(n):
    total += A[i][j]

print(f"Tổng các phần tử của ma trận A là: {total}")