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


def tim_ngay_ke_tiep(ngay_hien_tai):
    ngay_ke_tiep = ngay_hien_tai + timedelta(days=1)
    return ngay_ke_tiep


def main():
    ngay_hien_tai = nhap_ngay_thang_nam()
    ngay_ke_tiep = tim_ngay_ke_tiep(ngay_hien_tai)
    print("Ngày kế tiếp là: {}/{}/{}".format(ngay_ke_tiep.day, ngay_ke_tiep.month, ngay_ke_tiep.year))


main()