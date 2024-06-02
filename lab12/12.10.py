from datetime import datetime
from dateutil.relativedelta import relativedelta


def nhap_ngay(thu_tu):
    while True:
        try:
            ngay_str = input(f"Nhập ngày {thu_tu} (định dạng dd-mm-yyyy): ")
            ngay = datetime.strptime(ngay_str, "%d-%m-%Y")
            return ngay
        except ValueError:
            print("Định dạng ngày không hợp lệ. Vui lòng nhập lại.")


def tinh_khoang_cach(ngay1, ngay2):
    if ngay1 > ngay2:
        ngay1, ngay2 = ngay2, ngay1

    khoang_cach = relativedelta(ngay2, ngay1)
    return khoang_cach


def main():
    ngay1 = nhap_ngay("thứ nhất")
    ngay2 = nhap_ngay("thứ hai")
    khoang_cach = tinh_khoang_cach(ngay1, ngay2)

    print(
        "Khoảng cách giữa hai ngày là: {} năm, {} tháng, {} ngày".format(khoang_cach.years, khoang_cach.months, khoang_cach.days)
    )


main()