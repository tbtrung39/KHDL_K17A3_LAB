import math
x = int(input("nhập x:"))
fx = round((-x + math.sqrt(x**2 + 4))/(x**4 + 1)**(1/7), 2)
print(f"giá trị biểu thức = {fx}")