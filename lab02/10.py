def tinh_tien_thue_san(gio_bat_dau, gio_ket_thuc):
    tong_tien = 0
    for gio in range(gio_bat_dau, gio_ket_thuc):
        if gio < gio_bat_dau + 3:
            tong_tien += 100000
        else:
            tong_tien += 100000 * (0.75 ** (gio - gio_bat_dau))

    if 11 <= gio_bat_dau <= 15 and 11 <= gio_ket_thuc <= 15:
        tong_tien *= 0.9

    return tong_tien

gio_bat_dau = int(input("Nhập giờ bắt đầu thuê sân tập (từ 5 đến 22 giờ): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc thuê sân tập (từ 5 đến 22 giờ): "))

if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    tien_thue_san = tinh_tien_thue_san(gio_bat_dau, gio_ket_thuc)
    print("Số tiền khách hàng phải trả khi thuê sân từ", gio_bat_dau, "đến", gio_ket_thuc, "là:", tien_thue_san)
else:
    print("Giờ bắt đầu hoặc giờ kết thúc không hợp lệ.")