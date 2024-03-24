thoi_gian_su_dung = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
U = 220
I = 2.7
gia_dien = 7000
P = U * I

thoi_gian_su_dung_gio = thoi_gian_su_dung / 3600#đổi từ giây sang giờ
nang_luong_tieu_thu = P * thoi_gian_su_dung_gio / 1000#đổi từ kw sang kwm
tien_dien = nang_luong_tieu_thu * gia_dien

print("Tiền điện phải trả: ", tien_dien, "đồng")