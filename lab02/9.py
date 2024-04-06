so_kw = float(input("Nhập số: "))
if so_kw <= 100:
    don_gia = 2000
elif so_kw <= 200:
    don_gia = 2500
elif so_kw <= 300:
    don_gia = 3000
else:
    don_gia = 5000
tien_dien = so_kw * don_gia
print("Tiền điện cần thanh toán là:", tien_dien, "VNĐ")
