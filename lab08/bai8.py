import math
def chu_vi_hinh_tron(r):
    return 2 * math.pi * r
def dien_tich_hinh_tron(r):
    return math.pi * (r**2)
r = float(input("Nhập độ dài bán kính của hình tròn: "))
print("Chu vi của hình tròn là:",chu_vi_hinh_tron(r))
print("Diện tích của hình tròn là:",dien_tich_hinh_tron(r))