so_kw = float(input("Nhập số KW điện tiêu thụ: "))
if so_kw <= 100:
    tien_dien = so_kw * 2000
elif so_kw <= 200:
    tien_dien = 100*2000 + (so_kw - 100) * 2500
elif so_kw <= 300:
    tien_dien = 100*2000 + 100*2500 + (so_kw - 200) * 3000
else:
    tien_dien = 100*2000 + 100*2500 + 100*3000 + (so_kw - 300) * 5000
print("Số tiền điện cần thanh toán là:", tien_dien, "đồng")