n = int(input("tham nien cong tac :"))
luong_can_ban = 1350000
if n < 12 :
    luong = 2.34 * luong_can_ban
    print("luong",luong)
elif n < 36 :
    luong = 3.33 * luong_co_ban
    print("luong",luong)
elif n < 60 :
    luong = 3.66 * luong_can_ban
    print("luong",luong)
elif n >= 60 :
    luong = 3.99 * luong_can_ban
    print("luong",luong)
else:
    print("khong ton tai luong")