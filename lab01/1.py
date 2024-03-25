# Nhập bán kính và chiều cao từ bàn phím
r = float(input("Nhập bán kính: "))
h = float(input("Nhập chiều cao: "))

# Tính diện tích xung quanh, diện tích toàn phần và thể tích
pi = 3.14
dien_tich_xung_quanh = 2 * pi * r * h
dien_tich_toan_phan = 2 * pi * r * (r + h)
the_tich = pi * r**2 * h

# In kết quả
print("Diện tích xung quanh: ",dien_tich_xung_quanh)
print("Diện tích toàn phần: ",dien_tich_toan_phan)
print("Thể tích: ",the_tich)