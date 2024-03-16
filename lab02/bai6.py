n = int(input("Nhập số nguyên dương có 3 chữ số: "))
if n <100 or n>999:
    print("Phải là số có 3 chữ số, vui lòng nhập lại")
tram = n // 100
chuc = (n % 100) // 10
don_vi = n % 10
if tram == 1:
    doc_tram = "một trăm"
elif tram == 2:
    doc_tram = "hai trăm"
elif tram == 3:
    doc_tram = "ba trăm"
elif tram == 4:
    doc_tram = "bốn trăm"
elif tram == 5:
    doc_tram = "năm trăm"
elif tram == 6:
    doc_tram = "sáu trăm"
elif tram == 7:
    doc_tram = "bảy trăm"
elif tram == 8:
    doc_tram = "tám trăm"
elif tram == 9:
    doc_tram = "chín trăm"
if chuc == 0:
    doc_chuc = "lẻ" if don_vi != 0 else ""
elif chuc == 1:
    doc_chuc = "mười"
elif chuc == 2:
    doc_chuc = "hai mươi"
elif chuc == 3:
    doc_chuc = "ba mươi"
elif chuc == 4:
    doc_chuc = "bốn mươi"
elif chuc == 5:
    doc_chuc = "năm mươi"
elif chuc == 6:
    doc_chuc = "sáu mươi"
elif chuc == 7:
    doc_chuc = "bảy mươi"
elif chuc == 8:
    doc_chuc = "tám mươi"
elif chuc == 9:
    doc_chuc = "chín mươi"

if don_vi == 1:
    if chuc > 1:
        doc_don_vi = "mốt"
    else:
        doc_don_vi = "một"
elif don_vi == 2:
    doc_don_vi = "hai"
elif don_vi == 3:
    doc_don_vi = "ba"
elif don_vi == 4:
    doc_don_vi = "bốn"
elif don_vi == 5:
    if chuc == 0 or chuc == 1:
        doc_don_vi = "năm"
    else:
        doc_don_vi = "lăm"
elif don_vi == 6:
    doc_don_vi = "sáu"
elif don_vi == 7:
    doc_don_vi = "bảy"
elif don_vi == 8:
    doc_don_vi = "tám"
elif don_vi == 9:
    doc_don_vi = "chín"
else:
    doc_don_vi = ""

print("Số",n,"đọc là",doc_tram,doc_chuc,doc_don_vi)    