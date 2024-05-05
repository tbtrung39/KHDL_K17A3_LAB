def nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    else:
        return False
def so_ngay_toi_da_trong_thang(thang, nam):
    if thang in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif thang in {4, 6, 9, 11}:
        return 30
    elif thang == 2:
        if nam_nhuan(nam):
            return 29
        else:
            return 28
    else:
        return None  
try:
    thang = int(input("Nhập tháng (1-12): "))
    nam = int(input("Nhập năm: "))
    if thang < 1 or thang > 12:
        print("Tháng không hợp lệ.")
    else:
        ngay_toi_da = so_ngay_toi_da_trong_thang(thang, nam)
        if ngay_toi_da is None:
            print("Không xác định được số ngày tối đa của tháng.")
        else:
            print(f"Số ngày tối đa của tháng {thang} năm {nam} là {ngay_toi_da} ngày.")
except ValueError:
    print("Vui lòng nhập số nguyên cho tháng và năm.")
