gia_tien_dien = 7000
hieu_dien_the = 220
cuong_do_dong_dien = 2.7

cong_suat = hieu_dien_the * cuong_do_dong_dien / 1000
# Nhập thời gian sử dụng (giây)
thoi_gian_su_dung = float(input("Nhập thời gian sử dụng (giây): "))


# Thời gian sử dụng (giờ)
thoi_gian_su_dung_tinh_theo_gio = thoi_gian_su_dung / 3600
    
# Tiền điện (VND)
tien_dien = (cong_suat * thoi_gian_su_dung_tinh_theo_gio * gia_tien_dien) / 1000



print(f"Tiền điện phải trả là: {tien_dien} đồng")