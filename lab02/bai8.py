luong_co_ban = 1350000
TNCT =  int(input("nhap thang tham nien cua nhan vien: "))
if TNCT <1 :
    TNCT= int(input("nhap thang tham nien cua nhan vien"))
else:    
    if TNCT <12 :
        he_so = 2.34
    elif 12 <= TNCT and TNCT < 60:
        he_so = 3.33
    elif 36 <= TNCT and TNCT < 60 :
        he_so = 3.66
    elif TNCT >= 60:
        he_so = 3.99
    luong = he_so*luong_co_ban
    print("luong tham nien cua nhan vien", luong)