import math
a = float(input("Nhập V0 (m/s): "))
b = float(input("Nhập V chậm dần đều (m/s^2): "))
t = a / b
v=-t*math.log(4,5)+a**4
print(f"van toc: {v:.2f}")