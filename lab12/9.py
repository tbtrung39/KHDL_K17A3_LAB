from datetime import datetime, timedelta

def find_next_day(day):
    try:
        next_day = day + timedelta(days=1)
        return next_day
    except TypeError:
        print('Lỗi: Ngày không hợp lệ.')
        return None

def find_previous_day(day):
    try:
        previous_day = day - timedelta(days=1)
        return previous_day
    except TypeError:
        print('Lỗi: Ngày không hợp lệ.')
        return None

def find_weekday(day):
    try:
        weekdays = ['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ Nhật']
        weekday_index = day.weekday()
        return weekdays[weekday_index]
    except AttributeError:
        print('Lỗi: Ngày không hợp lệ.')
        return None

def main():
    day_input = input('Nhập ngày (ngày/tháng/năm): ')
    try:
        day = datetime.strptime(day_input, '%d/%m/%Y')
        next_day = find_next_day(day)
        previous_day = find_previous_day(day)
        weekday = find_weekday(day)

        if next_day and previous_day and weekday:
            print('Ngày kế tiếp:', next_day.strftime('%d/%m/%Y'))
            print('Ngày trước đó:', previous_day.strftime('%d/%m/%Y'))
            print('Ngày thuộc tuần thứ mấy:', weekday)
    except ValueError:
        print('Lỗi: Ngày không hợp lệ.')

if __name__ == '__main__':
    main()