import math
x = float(input("Nhap gia tri cua x: "))
result = math.log(x,4) + math.log(2,x)
print("gia tri cua bieu thuc la:", round(result, 2))