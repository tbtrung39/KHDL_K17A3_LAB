thoi_gian = float(input("Nhập thời gian sử dụng bóng đèn (S): "))
V = 220
I = 2.7
gia_tien_dien = 7000
P = V * I
thoi_gian_gio = thoi_gian / 3600
tien_dien = P * thoi_gian_gio * gia_tien_dien
print("Tiền điện phải trả là: ", round(tien_dien, 2), "đồng")