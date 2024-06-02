from datetime import datetime

def days_between_two_dates(date1, date2):
    try:
        date1 = datetime.strptime(date1, '%d-%m-%Y')
        date2 = datetime.strptime(date2, '%d-%m-%Y')

        delta = abs(date2 - date1)
        days = delta.days

        years, days = divmod(days, 365)
        months, days = divmod(days, 30)

        return years, months, days

    except ValueError:
        print('Lỗi: Ngày không hợp lệ.')
        return None, None, None

date1 = '01-01-2000'
date2 = '04-03-2023'
years, months, days = days_between_two_dates(date1, date2)

if years is not None and months is not None and days is not None:
    print(f'Hai ngày đó cách nhau {years} năm, {months} tháng và {days} ngày.')
