gio_bat_dau = int(input("Nhập giờ bắt đầu (từ 5 đến 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (từ 5 đến 22): "))
don_gia_3_gio_dau = 100000
don_gia_giam = 0.75 * don_gia_3_gio_dau
so_gio_thue = gio_ket_thuc - gio_bat_dau
if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    if gio_bat_dau >= 11 and gio_ket_thuc <= 15:
        tong_tien = (so_gio_thue * don_gia_giam) * 0.9
    elif so_gio_thue <= 3:
        tong_tien = so_gio_thue * don_gia_3_gio_dau
    else:
        tong_tien = (3 * don_gia_3_gio_dau) + ((so_gio_thue - 3) * don_gia_giam)
    print("Số tiền khách thuê sân tập phải trả là:", tong_tien, "đồng")
else:
    print("Giờ không hợp lệ! Vui lòng nhập lại.")