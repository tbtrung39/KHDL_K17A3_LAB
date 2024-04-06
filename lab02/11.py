ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10:
    so_ngay_trong_thang = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    so_ngay_trong_thang = 30
elif thang == 2:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        so_ngay_trong_thang = 29
    else:
        so_ngay_trong_thang = 28
else:
    print("Tháng không hợp lệ!")
if ngay < so_ngay_trong_thang:
    ngay += 1
else:
    ngay = 1
    if thang < 12:
        thang += 1
    else:
        thang = 1
        nam += 1
print("Ngày tiếp theo là:", ngay, "/", thang, "/", nam)
