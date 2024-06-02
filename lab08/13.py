def is_leap_year(year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False
def max_days_in_month(month, year):
    days_in_month = {
        1: 31,  # Tháng 1
        2: 29 if is_leap_year(year) else 28,  # Tháng 2
        3: 31,  # Tháng 3
        4: 30,  # Tháng 4
        5: 31,  # Tháng 5
        6: 30,  # Tháng 6
        7: 31,  # Tháng 7
        8: 31,  # Tháng 8
        9: 30,  # Tháng 9
        10: 31,  # Tháng 10
        11: 30,  # Tháng 11
        12: 31,  # Tháng 12
    }
    return days_in_month.get(month, 0)  # Trả về 0 nếu tháng không hợp lệ

# Ví dụ sử dụng:
month = 2  # Tháng 2
year = 2024
print(f"{year} là năm nhuận: {is_leap_year(year)}")
print(f"Số ngày tối đa của tháng {month} năm {year} là {max_days_in_month(month, year)} ngày.")
