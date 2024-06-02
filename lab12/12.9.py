from datetime import datetime, timedelta


def nhap_ngay_thang_nam():
    while True:
        try:
            ngay = int(input("Nhập ngày: "))
            thang = int(input("Nhập tháng: "))
            nam = int(input("Nhập năm: "))
            ngay_hien_tai = datetime(nam, thang, ngay)
            return ngay_hien_tai
        except ValueError:
            print("Ngày, tháng hoặc năm không hợp lệ. Vui lòng nhập lại.")


def tim_ngay_truoc(ngay_hien_tai):
    ngay_truoc = ngay_hien_tai - timedelta(days=1)
    return ngay_truoc


def tinh_tuan_trong_nam(ngay):
    tuan_thu = ngay.isocalendar()[1]
    return tuan_thu


def main():
    ngay_hien_tai = nhap_ngay_thang_nam()
    ngay_truoc = tim_ngay_truoc(ngay_hien_tai)
    tuan_thu = tinh_tuan_trong_nam(ngay_truoc)
    print("Ngày trước là: {}/{}/{}".format(ngay_truoc.day, ngay_truoc.month, ngay_truoc.year))
    print("Ngày trước thuộc tuần thứ: {}".format(tuan_thu))


main()