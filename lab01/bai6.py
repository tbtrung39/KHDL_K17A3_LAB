t = int(input("Nhập thời gian sử dụng (giây): "))
v = int(input("Nhập hiệu điện thế: "))
i = float(input("Nhập cường độ dòng điện: "))
gia_tien_dien = 7000
p = v * i
print("Công suất của dòng điện là: ", p) 
so_kwh = (p * (t/3600))/1000
tien_dien_phai_tra = so_kwh * gia_tien_dien
print("Tiền điện phải trả là: ", tien_dien_phai_tra)