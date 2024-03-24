so_KW = float(input("Nhập số KW điện tiêu thụ: "))
if so_KW < 100:
    tien_dien = so_KW * 2000
elif 101 < so_KW < 200:
    tien_dien = so_KW * 2500
elif 201 < so_KW < 300:
    tien_dien = so_KW * 3000
else: 
    tien_dien = so_KW * 5000
print("Số tiền điện phải trả là: ", tien_dien)
