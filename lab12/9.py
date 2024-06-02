while True:
    try:
        # Nhập ngày từ bàn phím
        ngay = input("Nhập ngày (định dạng DD-MM-YYYY): ")

        # Tách chuỗi ngày thành ngày, tháng, năm
        ngay, thang, nam = map(int, ngay.split('-'))

        # Kiểm tra xem ngày, tháng, năm có hợp lệ hay không
        if not (1 <= ngay <= 31 and 1 <= thang <= 12 and nam > 0):
            raise ValueError("Ngày không hợp lệ.")

        # Tính số ngày trong năm trước ngày đã nhập
        so_ngay = (thang - 1) * 30 + ngay

        # Tính tuần của năm
        tuan = so_ngay // 7 + 1

        # In tuần của năm
        print("Ngày này thuộc tuần thứ:", tuan)
    except ValueError as e:
        print(str(e))
