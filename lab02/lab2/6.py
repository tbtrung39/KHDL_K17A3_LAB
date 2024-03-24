so_nguyen = int(input("Nhập vào một số nguyên có ba chữ số: "))
if 100 <= so_nguyen <= 999:
    tram = so_nguyen // 100
    chuc = (so_nguyen % 100) // 10
    don_vi_so = so_nguyen % 10

    ket_qua = ""

    if tram > 0:
        if tram == 1:
            ket_qua += "một trăm "
        elif tram == 2:
            ket_qua += "hai trăm "
        elif tram == 3:
            ket_qua += "ba trăm "
        elif tram == 4:
            ket_qua += "bốn trăm "
        elif tram == 5:
            ket_qua += "năm trăm "
        elif tram == 6:
            ket_qua += "sáu trăm "
        elif tram == 7:
            ket_qua += "bảy trăm "
        elif tram == 8:
            ket_qua += "tám trăm "
        elif tram == 9:
            ket_qua += "chín trăm "

    if chuc > 1:
        if chuc == 2:
            ket_qua += "hai mươi "
        elif chuc == 3:
            ket_qua += "ba mươi "
        elif chuc == 4:
            ket_qua += "bốn mươi "
        elif chuc == 5:
            ket_qua += "năm mươi "
        elif chuc == 6:
            ket_qua += "sáu mươi "
        elif chuc == 7:
            ket_qua += "bảy mươi "
        elif chuc == 8:
            ket_qua += "tám mươi "
        elif chuc == 9:
            ket_qua += "chín mươi "
    elif chuc == 1:
        ket_qua += "mười "

    if don_vi_so > 1:
        if don_vi_so == 2:
            ket_qua += "hai"
        elif don_vi_so == 3:
            ket_qua += "ba"
        elif don_vi_so == 4:
            ket_qua += "bốn"
        elif don_vi_so == 5:
            ket_qua += "năm"
        elif don_vi_so == 6:
            ket_qua += "sáu"
        elif don_vi_so == 7:
            ket_qua += "bảy"
        elif don_vi_so == 8:
            ket_qua += "tám"
        elif don_vi_so == 9:
            ket_qua += "chín"
    elif don_vi_so == 1:
        ket_qua += "một"
    print(f"Cách đọc của số {so_nguyen} là: {ket_qua}.")
else:
    print("Số nguyên không hợp lệ")
