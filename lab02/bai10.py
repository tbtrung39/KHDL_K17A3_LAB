bat_dau = float(input("Nhập giờ bắt đầu: "))
ket_thuc = float(input("Nhập giờ kết thúc: "))
if 5 <= bat_dau <= ket_thuc <= 22:
    gio_thue = ket_thuc - bat_dau
    if gio_thue <= 3:
        tien_san = gio_thue * 100000
    elif gio_thue > 3:
        tien_san = 3 * 100000 + (gio_thue - 3) * (100000 * 0.75)
if 11 <= bat_dau <= ket_thuc <= 15:
    tien_san = tien_san * 0.9
print("Số tiền phải trả là: ", tien_san)