# Hàm chính
n = int(input("Nhập số thập phân (0-999): "))

if n < 0 or n > 999:
    print("Vui lòng nhập số từ 0 đến 999.")
else:
    hang_tram = n // 100
    n = n % 100
    hang_chuc = n // 10
    n = n % 10
    hang_don_vi = n

    ket_qua = ''

    if hang_tram != 0:
        if hang_tram == 1:
            ket_qua += 'một trăm '
        elif hang_tram == 2:
            ket_qua += 'hai trăm '
        elif hang_tram == 3:
            ket_qua += 'ba trăm '
        elif hang_tram == 4:
            ket_qua += 'bốn trăm '
        elif hang_tram == 5:
            ket_qua += 'năm trăm '
        elif hang_tram == 6:
            ket_qua += 'sáu trăm '
        elif hang_tram == 7:
            ket_qua += 'bảy trăm '
        elif hang_tram == 8:
            ket_qua += 'tám trăm '
        elif hang_tram == 9:
            ket_qua += 'chín trăm '

    if hang_chuc != 0:
        if hang_chuc == 1:
            ket_qua += 'mười '
        elif hang_chuc == 2:
            ket_qua += 'hai mươi '
        elif hang_chuc == 3:
            ket_qua += 'ba mươi '
        elif hang_chuc == 4:
            ket_qua += 'bốn mươi '
        elif hang_chuc == 5:
            ket_qua += 'năm mươi '
        elif hang_chuc == 6:
            ket_qua += 'sáu mươi '
        elif hang_chuc == 7:
            ket_qua += 'bảy mươi '
        elif hang_chuc == 8:
            ket_qua += 'tám mươi '
        elif hang_chuc == 9:
            ket_qua += 'chín mươi '

    if hang_don_vi != 0:
        if hang_don_vi == 1:
            if hang_chuc != 0:
                ket_qua += 'một'
            else:
                ket_qua += 'một'
        elif hang_don_vi == 2:
            ket_qua += 'hai'
        elif hang_don_vi == 3:
            ket_qua += 'ba'
        elif hang_don_vi == 4:
            ket_qua += 'bốn'
        elif hang_don_vi == 5:
            ket_qua += 'năm'
        elif hang_don_vi == 6:
            ket_qua += 'sáu'
        elif hang_don_vi == 7:
            ket_qua += 'bảy'
        elif hang_don_vi == 8:
            ket_qua += 'tám'
        elif hang_don_vi == 9:
            ket_qua += 'chín'

    print(ket_qua)
