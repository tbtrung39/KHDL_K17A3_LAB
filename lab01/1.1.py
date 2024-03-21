import math
r = float(input("Nhập bán kính khối trụ: "))
h = float(input("Nhập chiều cao khối trụ:"))
# tính diện tích xung quanh 
S = 2*math.pi*r*h
#tính diện tích toàn phần
A = 2*math.pi*r*(r+h)
#tính thể tích
V = math.pi*r**2*h

print("Diện tích xung quanh của khối trụ là: ",round(S,2))
print("Diện tích toàn phần của khối trụ là: ",round(A,2))
print("Thể tích của khối trụ là: ",round(V,2))
