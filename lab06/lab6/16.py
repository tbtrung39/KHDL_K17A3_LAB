
X = int(input("Nhập số hàng (X): "))
Y = int(input("Nhập số cột (Y): "))

while X <= 0 or Y <= 0:
    print("Vui lòng nhập số hàng và số cột lớn hơn 0!")
    X = int(input("Nhập số hàng (X): "))
    Y = int(input("Nhập số cột (Y): "))

# Tạo ma trận với số hàng (X) và số cột (Y) và giá trị của mỗi phần tử là i * j
ma_tran = []
for i in range(X):
    hang = []
    for j in range(Y):
        hang.append(i * j)
    ma_tran.append(hang)

# Hiển thị ma trận
print("Ma trận", X, "x", Y, "đã được tạo:")
for hang in ma_tran:
    print(hang)