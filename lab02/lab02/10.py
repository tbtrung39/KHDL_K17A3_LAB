gio_bd = int(input("Nhập giờ bắt đầu ( 5 -> 22): "))
gio_kt = int(input("Nhập giờ kết thúc (5 -> 22): "))

if gio_bd < 5 or gio_kt > 22 or gio_bd > gio_kt:
    print("Thời gian không hợp lệ.")
else:
    so_gio_thue = gio_kt - gio_bd
    tong_tien = 0
if gio_bd < gio_bd + 3 and gio_bd < gio_kt:
    if gio_bd + 3 < gio_kt:
        tong_tien+=100000*3
    else:
        tong_tien+=100000*(gio_kt-gio_bd)
    
    so_gio_tiep_theo = gio_kt-gio_bd-3
    if so_gio_tiep_theo > 0:
        tong_tien += 75000 * so_gio_tiep_theo


    if 11<=gio_bd and gio_bd<= 15:
        tong_tien *= 0.9

    print("Số tiền phải trả là:", tong_tien, "VNĐ")