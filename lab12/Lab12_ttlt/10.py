from datetime import datetime
def days_between_two_dates(date1, date2):
    # chuyen doi cac chuoi ngay thanh doi tuong datetime
    date1 = datetime.strptime(date1, '%d-%m-%Y')
    date2 = datetime.strptime(date2, '%d-%m-%Y')
    # tinh toan so giua 2 nhay
    days = abs(date2 - date1).days
    # tra cac gia tri ve ngay, thang ,nam
    years = days // 365
    days -= years * 365
    months = days // 30
    days -= months * 30
    return years, months, days
date1 = '01-01-2000'
date2 = '04-03-2023'
years, months, days = days_between_two_dates(date1, date2)
print(f"Hai ngày đó cách nhau {years} năm, {months} tháng và {days} ngày.")