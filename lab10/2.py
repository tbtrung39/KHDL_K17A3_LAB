from package.my_square import chuvihinhvuong, dien_tich_hinh_vuong

x = [2, 5, -3, 0, 7.5]
for a in x:
    chu_vi = chuvihinhvuong(a)
    dien_tich = dien_tich_hinh_vuong(a)
    if chu_vi is not None and dien_tich is not None:
        print(f"Hình vuông với cạnh {a}:")
        print(f"Chu vi: {chu_vi}")
        print(f"Diện tích: {dien_tich}")
    else:
        print(f"Cạnh {a} không hợp lệ cho một hình vuông")
