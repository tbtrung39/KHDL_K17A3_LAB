from datetime import datetime

# Hàm nhập ngày và chuyển đổi thành đối tượng datetime
def nhap_ngay(prompt):
    while True:
        try:
            ngay_input = input(prompt)
            ngay = datetime.strptime(ngay_input, '%d/%m/%Y')
            return ngay
        except ValueError:
            print("Định dạng ngày không hợp lệ, vui lòng nhập lại theo định dạng DD/MM/YYYY.")

# Hàm tính toán khoảng cách thời gian
def tinh_khoang_cach(ngay_bat_dau, ngay_ket_thuc):
    khoang_cach = ngay_ket_thuc - ngay_bat_dau
    nam = khoang_cach.days // 365
    thang = (khoang_cach.days % 365) // 30
    ngay = (khoang_cach.days % 365) % 30
    return nam, thang, ngay

# Chính
if __name__ == '__main__':
    ngay_bat_dau = nhap_ngay("Nhập ngày bắt đầu (DD/MM/YYYY): ")
    ngay_ket_thuc = nhap_ngay("Nhập ngày kết thúc (DD/MM/YYYY): ")

nam, thang, ngay = tinh_khoang_cach(ngay_bat_dau, ngay_ket_thuc)
print(f"Hai ngày cách nhau: {nam} năm, {thang} tháng, {ngay} ngày.")    