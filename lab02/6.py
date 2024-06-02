so = int(input("Nhập vào một số nguyên bất kỳ có 3 chữ số: "))
hang_tram = so//100
hang_chuc = (so//10)%10
hang_don_vi = so%10
if hang_tram == 1:
    hang_tram = "Một Trăm"
elif hang_tram == 2:
    hang_tram = "Hai Trăm"
elif hang_tram == 3:
    hang_tram = "Ba Trăm"
elif hang_tram == 4:
    hang_tram = "Bốn Trăm"
elif hang_tram == 5:
    hang_tram = "Năm Trăm"
elif hang_tram == 6:
    hang_tram = "Sáu Trăm"
elif hang_tram == 7:
    hang_tram = "Bảy Trăm"
elif hang_tram == 8:
    hang_tram = "Tám Trăm"
elif hang_tram == 9:
    hang_tram = "Chín Trăm"
if hang_chuc == 1:
    hang_chuc = "Mười"
elif hang_chuc == 2:
    hang_chuc = "Hai Mươi"
elif hang_chuc == 3:
    hang_chuc = "Ba Mươi"
elif hang_chuc == 4:
    hang_chuc = "Bốn Mươi"
elif hang_chuc == 5:
    hang_chuc = "Năm Mươi"
elif hang_chuc == 6:
    hang_chuc = "Sáu Mươi"
elif hang_chuc == 7:
    hang_chuc = "Bảy Mươi"
elif hang_chuc == 8:
    hang_chuc = "Tám Mươi"
elif hang_chuc == 9:
    hang_chuc = "Chín Mươi"
elif hang_chuc == 0 and hang_don_vi!=0:
    hang_chuc = "Linh"
if hang_don_vi ==1:
    hang_don_vi ="Một"
if hang_don_vi ==2:
    hang_don_vi ="Hai"
if hang_don_vi ==3:           
    hang_don_vi ="Ba"
if hang_don_vi ==4:
    hang_don_vi ="Bốn"
if hang_don_vi ==5:
    hang_don_vi ="Năm"
if hang_don_vi ==6:
    hang_don_vi ="Sáu"
if hang_don_vi ==7:
    hang_don_vi ="Bảy"
if hang_don_vi ==8:
    hang_don_vi ="Tám"
if hang_don_vi ==9:
    hang_don_vi ="Chín"
if hang_don_vi ==0:
    hang_don_vi =""
print("Số",so,"có cách đọc là:",hang_tram,hang_chuc,hang_don_vi)