thang = float(input("nhập tháng :"))
if thang == 2:
    print("tháng có 28 ngày hoặc 29 ngày.")
elif thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12 :
    print("tháng có 31 ngày.")    
elif thang == 4 or thang == 6 or thang == 9 or thang == 11 :
    print("các tháng có 30 ngày.")  
else:
    print("chỉ nhập từ 1 đến 12")      