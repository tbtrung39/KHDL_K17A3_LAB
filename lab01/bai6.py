# Phương trình bậc 2 có dạng a*x**2 +b*x + c = 0
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))

toa_do_dinh_x = -b / (2 * a)

toa_do_dinh_y = a * toa_do_dinh_x**2 + b * toa_do_dinh_x + c

print(f"Đỉnh của phương trình bậc 2 là:({toa_do_dinh_x}, {toa_do_dinh_y})")