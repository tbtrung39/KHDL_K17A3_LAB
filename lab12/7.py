def nam(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def ngay_mai(day, month, year):
    max_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if nam(year):
        max_days[2] = 29
    if day < max_days[month]:
        return day + 1, month, year
    else:
        if month < 12:
            return 1, month + 1, year
        else:
            return 1, 1, year + 1
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
            next_day_value = ngay_mai(day, month, year)
            print(f"Ngày kế tiếp là: {next_day_value[0]}/{next_day_value[1]}/{next_day_value[2]}")
            break
        except ValueError as ve:
            print(f"Lỗi: {ve}")
        except Exception as e:
            print(f"Lỗi: {e}")
if __name__ == "__main__":
    main()
