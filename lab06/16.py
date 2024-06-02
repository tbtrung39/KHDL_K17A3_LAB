# Nhập giá trị X, Y từ người dùng
X = int(input("Nhập giá trị X: "))
Y = int(input("Nhập giá trị Y: "))

# Tạo mảng 2 chiều theo yêu cầu
arr_2d = [[i*j for j in range(Y)] for i in range(X)]
print("Mảng 2 chiều:", arr_2d)
