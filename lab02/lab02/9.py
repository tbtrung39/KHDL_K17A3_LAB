kw_tieu_thu = float(input("Nhập số KW điện tiêu thụ: "))
if kw_tieu_thu<0:
    print('vui long nhap lai!')
if kw_tieu_thu >= 0 and kw_tieu_thu <= 100:
    don_gia = 2000
elif kw_tieu_thu <= 200:
    don_gia = 2500
elif kw_tieu_thu <= 300:
    don_gia = 3000
else:
    don_gia = 5000
tien_dien = kw_tieu_thu * don_gia
print(tien_dien,'dong')