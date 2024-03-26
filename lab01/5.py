# Nhập giá trị a, b, c từ bàn phím
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
c = float(input("Nhập giá trị của c: "))

# Kiểm tra a khác 0 (đảm bảo đây là phương trình bậc 2)
if a == 0:
    print("a phải khác 0.")
else:
    # Tính tọa độ x, y của đỉnh
    x = -b / (2*a)
    y = a*x**2 + b*x + c

    # In kết quả
    print("Đỉnh của phương trình là: ({:.2f}, {:.2f})".format(x, y))