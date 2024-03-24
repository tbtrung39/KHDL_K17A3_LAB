bat_dau = float(input("Nhập giờ bắt đầu(5->22): "))
ket_thuc = float(input("Nhập giờ kết thúc(5->22): "))
if 5<= bat_dau < ket_thuc <= 22:
    gio = ket_thuc-bat_dau
    tien= 0
    if gio <= 3:
        tien = gio*100000
    else:
        tien= 3*100000+(gio-3)*100000*0.75

    if 11<=bat_dau<ket_thuc<=15:
        tien *=0.9
    
    print(f"số tiền khách thuê sân tập phải trả là {tien} đồng")
else:
    print("vui lòng nhập đúng giờ")