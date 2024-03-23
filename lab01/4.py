hieu_dien_the = float(input("Nhap hieu dien the:"))
cuong_do_dien = float(input("Nhap cuong do dong dien :"))
thoi_gian_su_dung_giay = float(input("Nhap thoi gian su dung :"))
cong_suat = hieu_dien_the*cuong_do_dien
nang_luong_tieu_thu = (cong_suat * thoi_gian_su_dung_giay)/(3600*1000)
gia_tien_dien = 7000
tong_tien= nang_luong_tieu_thu*gia_tien_dien
print(f"nang luong tieu thu:{nang_luong_tieu_thu}")
print(f"tien dien phai tra:{tong_tien}") 