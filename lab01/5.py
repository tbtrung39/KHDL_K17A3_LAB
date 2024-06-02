# Nhập vào giá trị a, b, c của một phương trình bậc 2
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))

# Tính tọa độ x của đỉnh
x_vertex = -b / (2*a)

# Tính tọa độ y của đỉnh
y_vertex = a * x_vertex**2 + b * x_vertex + c

# Làm tròn đến số thập phân thứ hai và in ra ngay trong lệnh print
print("Đỉnh của phương trình bậc hai là: ({:.2f}, {:.2f})".format(x_vertex, y_vertex))
