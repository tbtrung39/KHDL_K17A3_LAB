try:
    # Nhập ngày từ bàn phím
    ngay, thang, nam = map(int, input("Nhập ngày (định dạng DD-MM-YYYY): ").split('-'))

    # Kiểm tra xem ngày, tháng, năm có hợp lệ hay không
    if not (1 <= ngay <= 31 and 1 <= thang <= 12 and nam > 0):
        raise ValueError("Ngày không hợp lệ.")

    # Tính ngày kế tiếp
    ngay += 1
    if ngay > 31:
        ngay = 1
        thang += 1
        if thang > 12:
            thang = 1
            nam += 1

    # In ngày kế tiếp
    print("Ngày kế tiếp là: %02d-%02d-%04d" % (ngay, thang, nam))
except ValueError as e:
    print(str(e))
