a = int(input("Nhập vào một số nguyên có 3 chữ số: "))
hang_tram= a // 100
hang_chuc= (a % 100) // 10
hang_dv=a% 10
so={
    1:"một",
    2:"hai",
    3:"ba",
    4:"bốn",
    5:"năm",
    6:"sáu",
    7:"bảy",
    8:"tám",
    9:"chín"
}
if a >= 100 and a <= 999 :
    if hang_chuc == 0 and hang_dv  == 0:
        print(f"{so[hang_tram]} trăm")
    elif hang_chuc == 0 :
        print(f"{so[hang_tram]} trăm linh {so[hang_dv]}")   
    elif hang_chuc == 1:
        print(f"{so[hang_tram]} trăm mười")
    elif hang_dv == 1:
        print(f"{so[hang_tram]} trăm {so[hang_chuc]} mươi mốt")
    elif hang_dv == 0:
        print(f"{so[hang_tram]} trăm {so[hang_chuc]} mươi")
    elif hang_dv != 0 :
        print(f"{so[hang_tram]} trăm {so[hang_chuc]} mươi {so[hang_dv]}")
else:
    ("Nhap sai")