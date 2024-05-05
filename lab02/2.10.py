gio_bd = float(input("Nhập giờ bắt đầu: "))
gio_kt = float(input("Nhập giờ kết thúc: "))
gio_bd >=5 and gio_kt <=22 or gio_kt > gio_bd
gio_thue = gio_kt - gio_bd
if gio_thue >=3:
  tien = ((gio_thue-3)*100000)*0.75
elif gio_thue ==3:
  tien = gio_thue * 100000
elif gio_thue >=11 and gio_thue <=15:
  tien = ((gio_thue * 100000)*0.75)*0.9
print("Tiền thuê bạn phải trả là: ", tien)