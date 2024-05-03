def leap_year_checker(x):
    if x % 4 ==0 and x % 100 ==0 and x % 400 ==0:
        print(x, "là năm nhuận")
    else:
        print(x, "không phải năm nhuận")
    
def days_in_a_month(x,y):
    if y ==1 or y ==3 or y ==5 or y==7 or y==8 or y ==10 or y ==12:
        print("Tháng có 31 ngày")
    elif y ==4 or y ==6 or y ==9 or y ==11:
        print("Tháng có 30 ngày")
    elif y ==2 and x % 4 ==0 and x % 100 ==0 and x % 400==0:
        print("Tháng có 29 ngày")
    else:
        print("Tháng có 28 ngày")

year = int(input("Nhập năm: "))
month = int(input("Nhập tháng: "))
print(leap_year_checker(year))
print(days_in_a_month(year, month))

