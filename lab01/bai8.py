import math

x = float(input("Nhập giá trị của x: "))

result = math.log(x, 4) + math.log(2, x)

print("Giá trị của biểu thức là:", round(result, 4))