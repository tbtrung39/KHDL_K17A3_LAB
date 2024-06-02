from datetime import datetime
def day_of_week(date):
    # Kiểm tra ngày và tháng của ngày đó
    if date.day == 1:
        # Nếu ngày là 1, tuần thứ mấy là Chủ Nhật
        return "Chủ Nhật"
    elif date.day == 2 or date.day == 3:
        # Nếu ngày là 2 hoặc 3, tuần thứ mấy là Thứ Hai
        return "Thứ Hai"
    elif date.day == 4 or date.day == 5:
        # Nếu ngày là 4 hoặc 5, tuần thứ mấy là Thứ Ba
        return "Thứ Ba"
    elif date.day == 6 or date.day == 7:
        # Nếu ngày là 6 hoặc 7, tuần thứ mấy là Thứ Tư
        return "Thứ Tư"
    elif date.day == 8:
        # Nếu ngày là 8, tuần thứ mấy là Thứ Năm
        return "Thứ Năm"
    elif date.day == 9 or date.day == 10:
        # Nếu ngày là 9 hoặc 10, tuần thứ mấy là Thứ Sáu
        return "Thứ Sáu"
    elif date.day == 11 or date.day == 12:
        # Nếu ngày là 11 hoặc 12, tuần thứ mấy là Thứ Bảy
        return "Thứ Bảy"
    else:
        # Nếu không phải là ngày cuối cùng của tháng, tăng ngày lên 1
        date += datetime.timedelta(days=1)
        return day_of_week(date)