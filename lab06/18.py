# Nhập số hàng m và số cột n từ người dùng
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

# Khởi tạo ma trận A và nhập giá trị cho từng phần tử
A = []
for i in range(m):
    row = [int(input(f"Nhập phần tử a[{i+1}][{j+1}]: ")) for j in range(n)]
    A.append(row)

print("Ma trận A:")
for row in A:
    print(row)
    
# Tính tổng các phần tử của ma trận A
sum_A = sum(sum(row) for row in A)
print("Tổng các phần tử của ma trận A:", sum_A)