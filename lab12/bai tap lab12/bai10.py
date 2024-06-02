from datetime import datetime

def calculate_difference(date1_str, date2_str):
    # Chuyển đổi chuỗi thành đối tượng ngày
    date1 = datetime.strptime(date1_str, "%d-%m-%y")
    date2 = datetime.strptime(date2_str, "%d-%m-%y")
    
    # Đảm bảo date1 là ngày nhỏ hơn
    if date1 > date2:
        date1, date2 = date2, date1

    # Tính toán số năm, tháng và ngày
    years = date2.year - date1.year
    months = date2.month - date1.month
    days = date2.day - date1.day

    # Điều chỉnh nếu số ngày âm
    if days < 0:
        months -= 1
        # Tính số ngày trong tháng trước đó
        previous_month = (date2.month - 1) if date2.month > 1 else 12
        previous_month_year = date2.year if date2.month > 1 else date2.year - 1
        previous_month_last_day = (datetime(previous_month_year, previous_month + 1, 1) - datetime(previous_month_year, previous_month, 1)).days
        days += previous_month_last_day

    # Điều chỉnh nếu số tháng âm
    if months < 0:
        years -= 1
        months += 12
    
    return years, months, days

# Nhập dữ liệu từ người dùng
date1_str = input("Nhập ngày đầu tiên (dd-mm-yy): ")
date2_str = input("Nhập ngày thứ hai (dd-mm-yy): ")

# Tính khoảng cách giữa hai ngày
years, months, days = calculate_difference(date1_str, date2_str)

# In kết quả
print(f"Khoảng cách giữa hai ngày là: {years} năm, {months} tháng, {days} ngày")
