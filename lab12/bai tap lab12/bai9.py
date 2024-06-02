from datetime import datetime

def week_of_year(day, month, year):
    input_date = datetime(year, month, day)
    
    week_number = input_date.isocalendar()[1]
    
    return week_number


day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

week_number = week_of_year(day, month, year)

print(f"Ngày {day}/{month}/{year} thuộc tuần thứ {week_number} trong năm.")
