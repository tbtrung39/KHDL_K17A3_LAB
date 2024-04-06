nam = int(input('Nhap so nam can biet: '))
thang = int(input('Nhap thang muon biet: '))
if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
    if thang == 2:
        print('thang co 29 ngay')
    elif thang > 0 and (thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12 ) and thang < 13 :
        print('Thang co 31 ngay')
    else:
        print('thang co 30 ngay')
else:
    if thang == 2:
        print('thang co 28 ngay')
    elif thang >0 and (thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12 ) and thang < 13:
        print('Thang co 31 ngay')
    else:
        print('thang co 30 ngay')