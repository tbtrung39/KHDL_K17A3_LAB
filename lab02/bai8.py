tnct = int(input("nhập tnct :"))
luong_can_ban = 1350000
if tnct < 12 :
    he_so = 2.34
    luong = he_so * luong_can_ban
    print("lương = ", luong)
elif tnct >= 12 and tnct <36 :
    he_so = 3.33
    luong = he_so * luong_can_ban
    print("lương = ",luong)
elif tnct >= 36 and tnct < 60 :
    he_so = 3.66
    luong = he_so * luong_can_ban
    print("lương = ", luong)
elif tnct >60 :
    he_so = 3.99
    luong = he_so * luong_can_ban
    print("lương = ", luong)
 