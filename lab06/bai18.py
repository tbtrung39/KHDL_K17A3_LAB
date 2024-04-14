m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
A = []

for i in range(m):
 row = []
 for j in range(n):
   aij = int(input(f"Nhập phần tử a{i+1}{j+1}: "))
   row.append(aij)
 A.append(row)
 
print("Ma trận A:")
for row in A:
 print(row)
 
tong = 0
for i in range(m):
 for j in range(n):
    tong += A[i][j]

print("Tổng các phần tử của ma trận A là:",tong)