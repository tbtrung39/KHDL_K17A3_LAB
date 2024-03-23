import math
r=float(input("Nhập bán kính của khối trụ: "))
h=float(input("Nhập chiều cao của khối trụ: "))
Sxq=2*math.pi*r*h
Stp=2*math.pi*r*(r+h)
V=math.pi*r**2*h

print(f"Diện tích xung quanh của khối trụ là: {Sxq:.2f}")
print(f"Diện tích toàn phần của khối trụ là: {Stp:.2f}")
print(f"Thể tích của khối trụ là: {V:.2f}")