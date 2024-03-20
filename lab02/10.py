# Nhập vào giờ bắt đầu và giờ kết thúc
start_hour = int(input("Nhập vào giờ bắt đầu (từ 5 đến 22): "))
end_hour = int(input("Nhập vào giờ kết thúc (từ giờ bắt đầu đến 22): "))

# Tính tổng số giờ thuê sân
total_hours = end_hour - start_hour

# Tính số tiền khách thuê sân tập phải trả
price = 0
discounted_price = 100000
for i in range(total_hours):
    if i < 3:
        price += 100000
    else:
        discounted_price *= 0.75
        price += discounted_price

# Kiểm tra nếu thời gian thuê sân từ 11 giờ đến 15 giờ thì được giảm giá 10%
if 11 <= start_hour <= 15 and 11 <= end_hour <= 15:
    price *= 0.9

print("Số tiền khách thuê sân tập phải trả là: {:.2f} đồng".format(price))
