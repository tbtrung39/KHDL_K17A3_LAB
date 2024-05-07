# Nhập thời gian sử dụng bóng đèn từ bàn phím (đơn vị: giây)
t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))

# Chuyển đổi thời gian từ giây sang giờ
t = t / 3600

# Tính công suất của bóng đèn (đơn vị: Watt)
P = 220 * 2.7

# Tính lượng điện năng tiêu thụ (đơn vị: kWh)
E = P * t / 1000

# Tính tiền điện phải trả (đơn vị: đồng)
cost = E * 7000

# In kết quả
print("Tiền điện phải trả là: {:.0f} đồng".format(cost))