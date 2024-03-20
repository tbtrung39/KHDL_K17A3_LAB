x = float(input("Nhập giá trị x: "))
import math
bieu_thuc = -x + math.sqrt(x**2 + 4) / pow(x**4 + 1, 1/7) 

print("Giá trị của biểu thức là: %.2f"%bieu_thuc)