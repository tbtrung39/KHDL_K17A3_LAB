gio_bat_dau = int(input('Nhap gio thue: '))
gio_ket_thuc = int(input('Nhap gio thue: '))
if not(5 <= gio_bat_dau <= 22) or not(5 <= gio_ket_thuc <= 22):
    print('Khong hop le')
elif gio_bat_dau >= gio_ket_thuc:
    print('Gio bat dau phai nho hon gio ket thuc')
else:
    so_gio_thue = gio_ket_thuc - gio_bat_dau
    gia_ban_dau = 100000
    tong_tien = 0
    if so_gio_thue <= 3:
        tong_tien = so_gio_thue * gia_ban_dau
    else:
        tong_tien = 3 * gia_ban_dau + (so_gio_thue - 3) * gia_ban_dau * 0.75
    if 11 <= gio_bat_dau <= 15 or 11 <= gio_ket_thuc <= 15:
        tong_tien *= 0.9
    print("So tien phai tra la:", tong_tien, "VND")