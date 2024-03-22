year = int(input("Nhập năm: "))
month = int(input("Nhập tháng: "))
day = int(input("Nhập ngày: "))
if month == 1:
    num_days = 31
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        num_days = 29
    else:
        num_days = 28
elif month == 3:
    num_days = 31
elif month == 4:
    num_days = 30
elif month == 5:
    num_days = 31
elif month == 6:
    num_days = 30
elif month == 7:
    num_days = 31
elif month == 8:
    num_days = 31
elif month == 9:
    num_days = 30
elif month == 10:
    num_days = 31
elif month == 11:
    num_days = 30
elif month == 12:
    num_days = 31
day += 1
if day > num_days:
    day = 1
    month += 1
    if month > 12:
        month = 1
        year += 1
print("Ngày tiếp theo là:", year, "-", month, "-", day)