from datetime import datetime
def tinh_khoang_cach_ngay(ngay1, ngay2):
    ngay1_obj = datetime.strptime(ngay1, "%d-%m-%Y")
    ngay2_obj = datetime.strptime(ngay2, "%d-%m-%Y")
    khoang_cach = ngay2_obj - ngay1_obj
    nam = khoang_cach.days // 365
    thang = (khoang_cach.days % 365) // 30
    ngay = (khoang_cach.days % 365) % 30
    return nam, thang, ngay
def main():
    try:
        ngay1 = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
        ngay2 = input("Nhập ngày thứ hai (dd-mm-yyyy): ")
        nam, thang, ngay = tinh_khoang_cach_ngay(ngay1, ngay2)
        print(f"Hai ngày cách nhau {nam} năm, {thang} tháng, {ngay} ngày.")
    except ValueError:
        print("Định dạng ngày không hợp lệ. Vui lòng nhập theo định dạng 'dd-mm-yyyy'.")
main()