n = int(input("Nhập số nguyên có ba chữ số: "))
tram = n // 100
chuc = (n % 100) // 10
donvi = n % 10
chuSo = ["không", "mốt", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
if tram == 0:
    print("không")
else:
    print(chuSo[tram], end=" ")
    print("trăm")
if chuc == 0:
    print("lẻ")
else:
    if chuc == 1:
        print("mười")
    else:
        print(chuSo[chuc], end=" ")
        print("mươi")
if donvi == 0:
    print("")
else:
    print(chuSo[donvi])
print("ngàn")