thang = int(input("Nhập tháng: "))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print ("Tháng",thang,"có 31 ngày")
elif thang in [4, 6, 9, 11]:
    print ("Tháng",thang,"có 30 ngày")
elif thang == 2:
    print ("Tháng",thang,"có 28 ngày vào năm không nhuận và 29 ngày vào năm nhuận")
else:
    print("Không có tháng",thang,"trong năm, vui lòng nhập lại")    