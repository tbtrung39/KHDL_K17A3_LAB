ngay = int(input("Nhập ngày:  "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm (không tính năm nhuận): "))

so_ngay_trong_thang = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Kt xem ngày đã cho có phải là ngày cuối của tháng hay không
if ngay == so_ngay_trong_thang[thang]:
    ngay = 1
    thang += 1
    # Nếu cộng tháng vào = 13, chuyển sang năm mới và đặt tháng về 1
    if thang == 13:
        thang = 1
        nam += 1
else:
    ngay += 1

print("Ngày tiếp theo là: ", ngay, "/", thang, "/", nam)