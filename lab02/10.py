gio_bat_dau = int(input("Nhập giờ bắt đầu: "))
if gio_bat_dau <5 or gio_bat_dau >22:
    print("Giờ bắt đầu không hợp lệ, vui lòng nhập lại")
gio_ket_thuc = int(input("Nhập giờ kết thúc: "))
if gio_ket_thuc >2 or gio_bat_dau <5:
    print("Giờ kết thúc không hợp lệ, vui lòng nhập lại")
so_gio_thue = gio_ket_thuc - gio_bat_dau
don_gia = 100000
giam_gia = 0.25
if so_gio_thue <= 3:
    tien = so_gio_thue * don_gia
else:
    tien = 3 * don_gia + (so_gio_thue - 3) * don_gia * (1 - giam_gia)
if gio_bat_dau >= 11 and gio_ket_thuc <= 15:
    tien = tien * 0.9
print("Số tiền khách hàng phải trả là: ",tien)