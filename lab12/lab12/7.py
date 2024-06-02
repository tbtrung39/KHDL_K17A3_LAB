def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def previous_date(day, month, year):
    days_in_month = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day -= 1
    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = days_in_month[month - 1]

    return day, month, year

def input_date():
    while True:
        try:
            day = int(input('Nhập ngày: '))
            month = int(input('Nhập tháng: '))
            year = int(input('Nhập năm: '))

            if day < 1 or month < 1 or month > 12 or year < 1 or day > 31:
                raise ValueError

            if day > 28 + is_leap_year(year) and month == 2:
                raise ValueError

            return day, month, year
        except ValueError:
            print('Ngày không hợp lệ, vui lòng nhập lại!')

def main():
    day, month, year = input_date()
    previous_day, previous_month, previous_year = previous_date(day, month, year)
    print('Ngày trước là: {:02d}/{:02d}/{}'.format(previous_day, previous_month, previous_year))

if __name__ == '__main__':
    main()
