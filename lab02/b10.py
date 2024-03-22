gio_bat_dau = int(input("Nhập giờ bắt đầu thuê sân (từ 5 đến 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc thuê sân (từ 5 đến 22): "))
if gio_bat_dau < 5 or gio_bat_dau > 22 or gio_ket_thuc < 5 or gio_ket_thuc > 22 or gio_bat_dau >= gio_ket_thuc:
    print("Thời gian thuê không hợp lệ.")
else:
    tong_tien = 0
    so_gio_dau_tien = min(3, gio_ket_thuc - gio_bat_dau)
    so_gio_con_lai = max(0, gio_ket_thuc - gio_bat_dau - 3)
    tong_tien += so_gio_dau_tien * 100000
    if so_gio_con_lai > 0:
        tong_tien += so_gio_con_lai * 75000
    if 11 <= gio_bat_dau <= 15 or 11 <= gio_ket_thuc <= 15:
        tong_tien *= 0.9
    print("Số tiền khách hàng phải trả là:", tong_tien, "VNĐ.")