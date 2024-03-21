import math
x = int(input("Nhập giá trị x: "))
fx = (-x + math.pow(x**2+4, 1/2)) / math.pow(x**4+1, 1/7)
print("Giá trị biểu thức fx là: ", round(fx,2))
