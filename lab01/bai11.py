import math

a = float(input("Nhập vào vận tốc chậm dần đều của ô tô: "))

# Tính thời gian dừng lại
thoi_gian_dung_lai = (math.log(5, 4) + a**4) / 

print(f"Thời gian ô tô dừng lại là: {thoi_gian_dung_lai} giây")
