from datetime import datetime, timedelta

def find_next_day(day):
    next_day = day + timedelta(days=1)
    return next_day

def find_previous_day(day):
    previous_day = day - timedelta(days=1)
    return previous_day

def find_weekday(day):
    weekday = day.weekday()
    if weekday == 0:
        return "Thứ Hai"
    elif weekday == 1:
        return "Thứ Ba"
    elif weekday == 2:
        return "Thứ Tư"
    elif weekday == 3:
        return "Thứ Năm"
    elif weekday == 4:
        return "Thứ Sáu"
    elif weekday == 5:
        return "Thứ Bảy"
    elif weekday == 6:
        return "Chủ Nhật"

day_input = input("Nhập ngày (ngày/tháng/năm): ")
day = datetime.strptime(day_input, "%d/%m/%Y")

next_day = find_next_day(day)
previous_day = find_previous_day(day)
weekday = find_weekday(day)

print("Ngày kế tiếp:", next_day.strftime("%d/%m/%Y"))
print("Ngày trước đó:", previous_day.strftime("%d/%m/%Y"))
print("Ngày thuộc tuần thứ mấy:", weekday)
