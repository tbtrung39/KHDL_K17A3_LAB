n = int(input("Nhập bậc của ma trận đơn vị: "))

# Sinh ma trận đơn vị và hiển thị kết quả
unit_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
print("Ma trận đơn vị bậc", n, ":\n")
for row in unit_matrix:
    print(row)