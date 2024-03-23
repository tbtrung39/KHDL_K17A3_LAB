import math
x = float(input("Nhap vao mot gia tri:"))
f = math.log(x,4) + math.log(2,x)
f = round(f,2)
print(f'F(x) = {f}')