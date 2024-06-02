def la_nam_nhuan(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def tinh_ngay_trong_nam(day, month, year):
    so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if la_nam_nhuan(year):
        so_ngay_trong_thang[1] = 29

    tong_so_ngay = sum(so_ngay_trong_thang[:month - 1]) + day
    return tong_so_ngay

def tinh_tuan_trong_nam(day, month, year):
    ngay_trong_nam = tinh_ngay_trong_nam(day, month, year)
    ngay_dau_tuan_dau_tien = tinh_ngay_trong_nam(1, 1, year) % 7
    thu = (ngay_trong_nam + ngay_dau_tuan_dau_tien - 1) % 7

    if thu == 0:
        return (ngay_trong_nam + ngay_dau_tuan_dau_tien - 1) // 7
    else:
        return (ngay_trong_nam + ngay_dau_tuan_dau_tien - 1) // 7 + 1

while True:
    try:
        day = int(input("Nhập ngày: "))
        month = int(input("Nhập tháng: "))
        year = int(input("Nhập năm: "))

        if day < 1 or month < 1 or month > 12 or year < 1:
            raise ValueError("Ngày hoặc tháng hoặc năm không hợp lệ.")

        tuan = tinh_tuan_trong_nam(day, month, year)
        print(f"Ngày {day}/{month}/{year} thuộc tuần thứ {tuan} trong năm {year}.")
        break
    except ValueError as ve:
        print("Lỗi:", ve)
    except Exception as e:
        print("Đã xảy ra lỗi:", e)