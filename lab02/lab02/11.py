ngay = int(input("Nhap ngay: "))
thang = int(input("Nhap thang: "))
nam = int(input("Nhap nam: "))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    if ngay < 31:
        ngay += 1
    else:
        if thang < 12:
            ngay = 1
            thang += 1
        else:
            ngay = 1
            thang = 1
            nam += 1
elif thang in [4, 6, 9, 11]:
    if ngay < 30:
        ngay += 1
    else:
        ngay = 1
        thang += 1
elif thang == 2:
    if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
        if ngay < 29:
            ngay += 1
        else:
            ngay = 1
            thang += 1
    else:
        if ngay < 28:
            ngay += 1
        else:
            ngay = 1
            thang += 1
print("Ngay tiep theo la: ", ngay, thang, nam)