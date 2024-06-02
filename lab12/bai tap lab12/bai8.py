from datetime import datetime, timedelta

def next_day(day, month, year):
    input_date = datetime(year, month, day)
    
    # Tính toán ngày kế tiếp bằng cách cộng thêm 1 ngày
    next_date = input_date + timedelta(days= -1)
    
    # Trả về ngày kế tiếp dưới dạng ngày, tháng, năm
    return next_date.day, next_date.month, next_date.year


day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

# Tìm ngày kế tiếp
day_next, month_next, year_next = next_day(day, month, year)

print(f"Ngày trước của ngày vừa nhập là: {day_next}/{month_next}/{year_next}")
