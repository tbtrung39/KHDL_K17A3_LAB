num = input("Nhập vào một số nguyên có ba chữ số: ")

if len(num) == 3 and num.isdigit():
    hang_tram = int(num[0])
    hang_chuc = int(num[1])
    hang_don_vi = int(num[2])
    
    hang_tram_text = ''
    hang_chuc_text = ''
    hang_don_vi_text = ''
    
    if hang_tram == 1:
        hang_tram_text = 'một trăm'
    elif hang_tram == 2:
        hang_tram_text = 'hai trăm'
    elif hang_tram == 3:
        hang_tram_text = 'ba trăm'
    elif hang_tram == 4:
        hang_tram_text = 'bốn trăm'
    elif hang_tram == 5:
        hang_tram_text = 'năm trăm'
    elif hang_tram == 6:
        hang_tram_text = 'sáu trăm'
    elif hang_tram == 7:
        hang_tram_text = 'bảy trăm'
    elif hang_tram == 8:
        hang_tram_text = 'tám trăm'
    elif hang_tram == 9:
        hang_tram_text = 'chín trăm'
        
    if hang_chuc == 0:
        hang_chuc_text = ''
    elif hang_chuc == 1:
        hang_chuc_text = 'mười'
    elif hang_chuc == 2:
        hang_chuc_text = 'hai mươi'
    elif hang_chuc == 3:
        hang_chuc_text = 'ba mươi'
    elif hang_chuc == 4:
        hang_chuc_text = 'bốn mươi'
    elif hang_chuc == 5:
        hang_chuc_text = 'năm mươi'
    elif hang_chuc == 6:
        hang_chuc_text = 'sáu mươi'
    elif hang_chuc == 7:
        hang_chuc_text = 'bảy mươi'
    elif hang_chuc == 8:
        hang_chuc_text = 'tám mươi'
    elif hang_chuc == 9:
        hang_chuc_text = 'chín mươi'
        
    if hang_don_vi == 0:
        hang_don_vi_text = ''
    elif hang_don_vi == 1:
        if hang_chuc == 0:
            hang_don_vi_text = 'một'
        else:
            hang_don_vi_text = 'mốt'
    elif hang_don_vi == 2:
        hang_don_vi_text = 'hai'
    elif hang_don_vi == 3:
        hang_don_vi_text = 'ba'
    elif hang_don_vi == 4:
        hang_don_vi_text = 'bốn'
    elif hang_don_vi == 5:
        if hang_chuc == 0:
            hang_don_vi_text = 'năm'
        else:
            hang_don_vi_text = 'lăm'
    elif hang_don_vi == 6:
        hang_don_vi_text = 'sáu'
    elif hang_don_vi == 7:
        hang_don_vi_text = 'bảy'
    elif hang_don_vi == 8:
        hang_don_vi_text = 'tám'
    elif hang_don_vi == 9:
        hang_don_vi_text = 'chín'
        
    print(f"{hang_tram_text} {hang_chuc_text} {hang_don_vi_text}")
else:
    print("Số nhập không hợp lệ.")