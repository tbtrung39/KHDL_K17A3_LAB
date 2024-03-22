gio_bat_dau = int(input("Nhập giờ bắt đầu (từ 5 đến 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (từ 5 đến 22): "))
if gio_bat_dau < 5 or gio_bat_dau > 22 or gio_ket_thuc < 5 or gio_ket_thuc > 22 or gio_bat_dau > gio_ket_thuc:
    print("Giờ không hợp lệ. Vui lòng nhập lại.")
else:
    gia_tien_gio_dau_tien = 100000
    so_gio_giam_gia = 3
    giam_gia = 0.1 if 11 <= gio_bat_dau <= 15 else 0
    tong_tien = min(gio_ket_thuc - gio_bat_dau, so_gio_giam_gia) * gia_tien_gio_dau_tien
    if gio_ket_thuc - gio_bat_dau > so_gio_giam_gia:
        tong_tien += max(0, gio_ket_thuc - gio_bat_dau - so_gio_giam_gia) * gia_tien_gio_dau_tien * 0.75
    if 11 <= gio_bat_dau <= 15:
        tong_tien *= 0.9
    print("Số tiền khách hàng phải trả: {} đồng".format(tong_tien))