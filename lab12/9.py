from datetime import datetime
def tuan_trong_nam(ngay, thang, nam):
    date_object = datetime(nam, thang, ngay)
    so_tuan = date_object.isocalendar()[1]
    return so_tuan
def main():
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        datetime(nam, thang, ngay)
        tuan = tuan_trong_nam(ngay, thang, nam)
        print(f"Ngày {ngay}/{thang}/{nam} thuộc tuần thứ {tuan} trong năm.")
    except ValueError:
        print("Ngày, tháng, năm không hợp lệ.")
main()