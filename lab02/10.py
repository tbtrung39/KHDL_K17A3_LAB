gio_bat_dau = int(input("Nhập giờ bắt đầu thuê sân (từ 5 đến 22 giờ): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc thuê sân (từ 5 đến 22 giờ): "))
gia_ban_dau = 100000
so_gio_thue = gio_ket_thuc - gio_bat_dau
tong_tien = 0

for gio in range(gio_bat_dau, gio_ket_thuc):
    if gio < gio_bat_dau + 3:
        tong_tien += gia_ban_dau
    else: 
        tong_tien += gia_ban_dau * 0.75
if 11 <= gio_bat_dau <= 15 and 11 <= gio_ket_thuc <= 15:
    tong_tien *= 0.9
print("Số tiền khách hàng cần trả là:", tong_tien, "VNĐ")
