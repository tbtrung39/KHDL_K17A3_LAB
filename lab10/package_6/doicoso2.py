def xoa_ki_tu(chuoi):
    a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    chuoi_moi = ""
    for i in chuoi:
        if i.upper() in a:
            chuoi_moi += i
    return chuoi_moi

def phat_hien_he(chuoi):
    chuoi = chuoi.upper()
    if all(c in '01' for c in chuoi):
        return 2
    elif all(c in '01234567' for c in chuoi):
        return 8
    elif all(c in '0123456789ABCDEF' for c in chuoi):
        return 16
    else:
        return "Không xác định được cơ số"

def he_2_sang_10(chuoi):
    try:
        return int(chuoi, 2)
    except ValueError:
        return "Chuỗi không hợp lệ cho cơ số 2"
def he_8_sang_10(chuoi):
    try:
        return int(chuoi, 8)
    except ValueError:
        return "Chuỗi không hợp lệ cho cơ số 8"

def he_16_sang_10(chuoi):
    try:
        return int(chuoi, 16)
    except ValueError:
        return "Chuỗi không hợp lệ cho cơ số 16"
    