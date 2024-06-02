def la_nam_nhuan(nam):
    # Kiểm tra năm nhuận
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

def tim_ngay_truoc(ngay, thang, nam):
    # Số ngày tối đa trong từng tháng
    so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Nếu là năm nhuận thì tháng 2 có 29 ngày
    if la_nam_nhuan(nam):
        so_ngay_trong_thang[1] = 29

    ngay -= 1  # Giảm ngày đi 1

    if ngay < 1:
        thang -= 1
        if thang < 1:
            thang = 12
            nam -= 1
        ngay = so_ngay_trong_thang[thang - 1]

    return ngay, thang, nam

def nhap_ngay():
    while True:
        try:
            ngay = int(input("Nhập ngày: "))
            thang = int(input("Nhập tháng: "))
            nam = int(input("Nhập năm: "))

            if ngay < 1 or thang < 1 or thang > 12 or nam < 1:
                raise ValueError

            # Số ngày tối đa trong từng tháng
            so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            # Nếu là năm nhuận thì tháng 2 có 29 ngày
            if la_nam_nhuan(nam):
                so_ngay_trong_thang[1] = 29

            if ngay > so_ngay_trong_thang[thang - 1]:
                raise ValueError

            return ngay, thang, nam
        except ValueError:
            print("Ngày không hợp lệ, vui lòng nhập lại!")

def main():
    ngay, thang, nam = nhap_ngay()
    ngay_truoc, thang_truoc, nam_truoc = tim_ngay_truoc(ngay, thang, nam)
    print("Ngày trước là: {:02d}/{:02d}/{}".format(ngay_truoc, thang_truoc, nam_truoc))

if __name__ == "__main__":
    main()