kW = int(input("Nhập số điện KW tiêu thụ: "))
if kW >=0 and kW <=100:
  don_gia = 2000
elif kW >=101 and kW <=200:
  don_gia = 2500
elif kW >=201 and kW <=300:
  don_gia = 3000
elif kW >300:
  don_gia = 5000
tien_dien = don_gia * kW
print("Tiền điện phải trả là: ", tien_dien)