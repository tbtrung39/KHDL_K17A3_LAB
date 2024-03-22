import math
van_toc_ban_dau = float(input("Nhập vào vận tốc ban đầu của xe o to(m/s): "))
a = float(input("Nhập vào giả tốc của xe ô tô (m/s^2): "))
t = (van_toc_ban_dau / a) * (1 - math.exp(-a))
quang_duong_dung_lai = (-t * math.log(5,4)) + a**4
print(f"Thời gian để ô tô dừng lại: {round(t, 2)} giây")
print(f"Quãng đường dừng lại: {round(quang_duong_dung_lai, 2)} mét")