tnct = int(input("Nhập tháng thâm niên công tác: "))
luong_can_ban = 1350000
if tnct < 1:
    print("Tháng công tác không hợp lệ, vui lòng nhập lại")
else:
    if tnct <12:
        he_so = 2.34
    elif tnct >=12 and tnct <36:
        he_so = 3.33
    elif tnct>=36 and tnct<60:
        he_so = 3.66
    else:
        he_so = 3.99
    luong = he_so * luong_can_ban
    print("Lương của nhân viên là: ",luong)          