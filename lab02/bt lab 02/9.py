so_kw = int(input("Nhập số điện: "))
if so_kw < 100:
    don_gia = 2000
elif 101 <= so_kw <= 200:
    don_gia = 2500
elif 201 <= so_kw <= 300:
    don_gia = 3000
else:
    don_gia = 5000

if so_kw >= 0:
    tien_dien = so_kw * don_gia
    print("Tiền điện cần thanh toán:", tien_dien, "đồng")
else:
    print("Số KW điện tiêu thụ không hợp lệ! Vui lòng nhập lại.")   