h = float(input("Nhập chiều cao của hình trụ: "))
r = float(input("Nhập bán kính của hình trụ: "))

import math
dien_tich_xung_quanh = 2*math.pi*r*h
dien_tich_toan_phan = 2*math.pi*math.pow(r,2) + 2*math.pi*r*h
the_tich_hinh_tru = math.pi*math.pow(r,2)*h

print("Diện tích xung quanh của hình trụ là: %.2f"%dien_tich_xung_quanh)
print("Diện tích toàn phần của hình trụ là: %.2f"%dien_tich_toan_phan)
print("Thể tích của hình trụ là: %.2f"%the_tich_hinh_tru)