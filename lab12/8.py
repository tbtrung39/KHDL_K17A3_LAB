def nam(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def ngay(day, month, year):
    max_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if nam(year):
        max_days[2] = 29
    if day > 1:
        return day - 1, month, year
    else:
        if month > 1:
            return max_days[month - 1], month - 1, year
        else:
            return max_days[12], 12, year - 1
def main():
    while True:
        try:
            day = int(input("Nhập ngày: "))
            month = int(input("Nhập tháng: "))
            year = int(input("Nhập năm: "))
            if month < 1 or month > 12:
                raise ValueError("Tháng không hợp lệ.")
            if day < 1 or day > 31:
                raise ValueError("Ngày không hợp lệ.")
            day_value = ngay(day, month, year)
            print(f"Ngày trước đó là: {day_value[0]}/{day_value[1]}/{day_value[2]}")
            break
        except ValueError as ve:
            print(f"Lỗi: {ve}")
        except Exception as e:
            print(f"Lỗi: {e}")
if __name__ == "__main__":
    main()
