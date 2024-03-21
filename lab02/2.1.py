month =int(input("Nhập tháng: "))
if month ==2:
  print("Tháng có 28 hoặc 29 ngày")
elif month ==4 or month ==6 or month ==9 or month ==11:
  print("Tháng có 30 ngày")
elif month ==1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12:
  print("Tháng có 31 ngày")