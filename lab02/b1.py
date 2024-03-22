thang = int(input("nhap vao thang: "))
nam = int(input("nhap vao nam: "))
if thang ==1:
    print("thang có 31 ngay")
if thang ==3:
    print("thang có 31 ngay")
if thang ==5:
    print("thang có 31 ngay")
if thang ==7:
    print("thang có 31 ngay")
if thang ==8:
    print("thang có 31 ngay")
if thang ==10:
    print("thang có 31 ngay")
if thang ==12:
    print("thang có 31 ngay")
elif thang ==4:
    print("thang co 30 ngay")
elif thang ==6:
    print("thang co 30 ngay")
elif thang ==9:
    print("thang co 30 ngay")
elif thang ==11:
    print("thang co 30 ngay")
elif thang == 2:
    if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 == 0):
        print("thang 2 co 29 ngay")
    else:
        print("thang 2 co 28 ngay")
else:
    print("so thang khong hop le")