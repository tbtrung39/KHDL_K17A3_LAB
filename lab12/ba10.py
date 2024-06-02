from datetime import datetime
def days_between_two_dates(date1, date2):
    # chuyển đổi các chuỗi ngày thành các đối tượng datetime
    date1 = datetime.strptime(date1, '%d-%m-%Y')
    date2 = datetime.strptime(date2, '%d-%m-%Y')
    # tính toán số ngày giữa hai ngày
    days = abs(date2 - date1).days
    # trả về số năm, tháng và ngày
    years = days // 365
    days -= years * 365
    months = days // 30
    days -= months * 30
    return years, months, days
date1 = '01-01-2000'
date2 = '04-03-2023'
years, months, days = days_between_two_dates(date1, date2)
print(f"Hai ngày đó cách nhau {years} năm, {months} tháng và {days} ngày.")