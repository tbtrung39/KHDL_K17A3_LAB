from datetime import datetime

def days_between_two_dates(date1, date2):
    try:
        date1 = datetime.strptime(date1, '%d/%m/%Y')
        date2 = datetime.strptime(date2, '%d/%m/%Y')
        days = abs(date2 - date1).days
        years = days // 365
        days %= 365
        months = days // 30
        days %= 30
        return years, months, days
    except ValueError as ve:
        print(f"Lỗi: {ve}")
        return None, None, None

date1 = input("Nhập ngày thứ nhất (ngày/tháng/năm): ")
date2 = input("Nhập ngày thứ hai (ngày/tháng/năm): ")
years, months, days = days_between_two_dates(date1, date2)
if years is not None:
    print(f"Hai ngày đó cách nhau {years} năm, {months} tháng và {days} ngày.")
