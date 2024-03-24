thang= int(input("Nhập tháng là: "))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    print(f"{thang} là tháng có 31 ngày")
elif thang == 2:
    print(f"{thang} là tháng có 28 ngày hoặc 29 nếu là năm nhuận")
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    print(f"{thang} là tháng có 30 ngày")