so_nguyen = int(input("Nhập số nguyên có ba chữ số: "))
hang_tram_so = so_nguyen // 100
hang_chuc_so = (so_nguyen % 100) // 10
hang_don_vi_so = so_nguyen % 10
if hang_tram_so == 1:
    print("một trăm", end=" ")
elif hang_tram_so == 2:
    print("hai trăm", end=" ")
elif hang_tram_so == 3:
    print("ba trăm", end=" ")
elif hang_tram_so == 4:
    print("bốn trăm", end=" ")
elif hang_tram_so == 5:
    print("năm trăm", end=" ")
elif hang_tram_so == 6:
    print("sáu trăm", end=" ")
elif hang_tram_so == 7:
    print("bảy trăm", end=" ")
elif hang_tram_so == 8:
    print("tám trăm", end=" ")
elif hang_tram_so == 9:
    print("chín trăm", end=" ")

if hang_chuc_so == 1:
    if hang_don_vi_so == 0:
        print("mười")
    elif hang_don_vi_so == 1:
        print("mười một")
    elif hang_don_vi_so == 2:
        print("mười hai")
    elif hang_don_vi_so == 3:
        print("mười ba")
    elif hang_don_vi_so == 4:
        print("mười bốn")
    elif hang_don_vi_so == 5:
        print("mười lăm")
    elif hang_don_vi_so == 6:
        print("mười sáu")
    elif hang_don_vi_so == 7:
        print("mười bảy")
    elif hang_don_vi_so == 8:
        print("mười tám")
    elif hang_don_vi_so == 9:
        print("mười chín")
elif hang_chuc_so == 2:
    print("hai mươi", end=" ")
elif hang_chuc_so == 3:
    print("ba mươi", end=" ")
elif hang_chuc_so == 4:
    print("bốn mươi", end=" ")
elif hang_chuc_so == 5:
    print("năm mươi", end=" ")
elif hang_chuc_so == 6:
    print("sáu mươi", end=" ")
elif hang_chuc_so == 7:
    print("bảy mươi", end=" ")
elif hang_chuc_so == 8:
    print("tám mươi", end=" ")
elif hang_chuc_so == 9:
    print("chín mươi", end=" ")

if hang_chuc_so != 1 and hang_don_vi_so != 0:
    if hang_don_vi_so == 1:
        print("mốt")
    elif hang_don_vi_so == 5:
        print("lăm")
    else:
        print(hang_don_vi_so)