# viết chương trình nhập vào 1 số nguyên có 3 chữ số 
# hãy in ra cách đọc của số nguyên này
x = int(input("Nhập 1 số nguyên có 3 chữ số:"))
hang_tram= (x//100)%10
if hang_tram == 1:
    hang_tram_1 ="một"
elif hang_tram == 2:
    hang_tram_1 ="hai"
elif hang_tram == 3:
    hang_tram_1 ="ba"
elif hang_tram == 4:
    hang_tram_1 ="bốn"
elif hang_tram == 5:
    hang_tram_1 =" năm"
elif hang_tram == 6:
    hang_tram_1 ="sáu"
elif hang_tram == 7:
    hang_tram_1 ="bảy"
elif hang_tram == 8:
    hang_tram_1 ="tám"
elif hang_tram == 9:
    hang_tram_1 =" chín"
hang_chuc = (x//10)%10
if  hang_chuc == 1:
    hang_chuc_1 ="mười"
elif hang_chuc == 2:
    hang_chuc_1 = "hai mươi"
elif hang_chuc == 3:
    hang_chuc_1 = "ba mươi"
elif hang_chuc == 4:
    hang_chuc_1 = "bốn mươi"
elif hang_chuc == 5:
    hang_chuc_1 = "năm mươi"
elif hang_chuc == 6:
    hang_chuc_1 = "sáu mươi"
elif hang_chuc == 7:
    hang_chuc_1 = "bảy mươi"
elif hang_chuc == 8:
    hang_chuc_1 = "tám mươi"
elif hang_chuc == 9:
    hang_chuc_1 = "chín mươi"
hang_don_vi = x%10
if hang_don_vi == 1:
    if hang_chuc == 1 or hang_chuc == 0:
        hang_don_vi_1 ="một"
    else:
        hang_don_vi_1 ="mốt"
elif hang_don_vi == 2:
    hang_don_vi_1 = "hai"
elif hang_don_vi == 3:
    hang_don_vi_1 ="ba"
elif hang_don_vi == 4:
    hang_don_vi_1 ="bốn"
elif hang_don_vi == 5:
    if hang_chuc == 0:
        hang_don_vi_1 ="năm"
    elif hang_chuc != 0: 
        hang_don_vi_1 ="lăm"   
elif hang_don_vi == 6:
    hang_don_vi_1 ="sáu"
elif hang_don_vi == 7:
    hang_don_vi_1 ="bảy"
elif hang_don_vi == 8:
    hang_don_vi_1 ="tám"
elif hang_don_vi == 9:
    hang_don_vi_1 ="chín"
if (x//10)%10 == 0 and x%10 != 0:
    hang_chuc_3 = "linh"
    print(f"cách đọc: {hang_tram_1} trăm {hang_chuc_3} {hang_don_vi_1}")
elif (x%10)%10 == 0 and x% 100 !=0:
    print(f"cách đọc: {hang_tram_1} trăm {hang_chuc_1}")
elif x % 100 == 0:
    print(f"cách đọc: {hang_tram_1} trăm")
elif hang_chuc !=0 :
    print(f"cách đọc số nguyên : {hang_tram_1} trăm {hang_chuc_1} {hang_don_vi_1}")
