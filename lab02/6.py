# Nhập số nguyên có ba chữ số từ bàn phím
n = int(input("Nhập vào số nguyên có ba chữ số: "))

# Xác định hàng trăm
hang_tram = n // 100
if hang_tram == 1:
    print("Một trăm")
elif hang_tram == 2:
    print("Hai trăm")
elif hang_tram == 3:
    print("Ba trăm")
elif hang_tram == 4:
    print("Bốn trăm")
elif hang_tram == 5:
    print("Năm trăm")
elif hang_tram == 6:
    print("Sáu trăm")
elif hang_tram == 7:
    print("Bảy trăm")
elif hang_tram == 8:
    print("Tám trăm")
elif hang_tram == 9:
    print("Chín trăm")

# Xác định hàng chục
hang_chuc = (n // 10) % 10
if hang_chuc == 1:
    print("mười")
elif hang_chuc == 2:
    print("hai mươi")
elif hang_chuc == 3:
    print("ba mươi")
elif hang_chuc == 4:
    print("bốn mươi")
elif hang_chuc == 5:
    print("năm mươi")
elif hang_chuc == 6:
    print("sáu mươi")
elif hang_chuc == 7:
    print("bảy mươi")
elif hang_chuc == 8:
    print("tám mươi")
elif hang_chuc == 9:
    print("chín mươi")

# Xác định hàng đơn vị
hang_don_vi = n % 10
if hang_don_vi == 1:
    print("một")
elif hang_don_vi == 2:
    print("hai")
elif hang_don_vi == 3:
    print("ba")
elif hang_don_vi == 4:
    print("bốn")
elif hang_don_vi == 5:
    print("lăm")
elif hang_don_vi == 6:
    print("sáu")
elif hang_don_vi == 7:
    print("bảy")
elif hang_don_vi == 8:
    print("tám")
elif hang_don_vi == 9:
    print("chín")