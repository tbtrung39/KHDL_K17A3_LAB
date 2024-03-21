U = 220
I = 2.7
t = float(input("Thời gian sử dụng bóng đèn(giây) là: "))
tien_dien = ((U*I*t)/3600000)*7000
print("Tiền điện bạn phải trả là: ",tien_dien)