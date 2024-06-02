import re
def nhap_chuoi():
    chuoi = input("Nhập vào một chuỗi ký tự: ")
    return chuoi
def loai_bo_ky_tu(chuoi):
    chuoi_ket_qua = re.sub(r'[^0-9A-F]', '', chuoi, flags=re.IGNORECASE)
    print(f"Chuỗi kết quả sau khi loại bỏ các ký tự không hợp lệ: {chuoi_ket_qua}")
    return chuoi_ket_qua
def xac_dinh_co_so(chuoi):
    if re.match(r'^[01]+$', chuoi):
        return 2
    elif re.match(r'^[0-7]+$', chuoi):
        return 8
    elif re.match(r'^[0-9A-F]+$', chuoi, flags=re.IGNORECASE):
        return 16
    else:
        return None
def chuyen_co_so_2_sang_10(chuoi):
    return int(chuoi, 2)
def chuyen_co_so_8_sang_10(chuoi):
    return int(chuoi, 8)
def chuyen_co_so_16_sang_10(chuoi):
    return int(chuoi, 16)
def hien_thi_ket_qua(chuoi):
    co_so = xac_dinh_co_so(chuoi)
    if co_so == 2:
        print(f"Chuỗi '{chuoi}' là chuỗi số thuộc cơ số 2.")
        print(f"Giá trị cơ số 10: {chuyen_co_so_2_sang_10(chuoi)}")
    elif co_so == 8:
        print(f"Chuỗi '{chuoi}' là chuỗi số thuộc cơ số 8.")
        print(f"Giá trị cơ số 10: {chuyen_co_so_8_sang_10(chuoi)}")
    elif co_so == 16:
        print(f"Chuỗi '{chuoi}' là chuỗi số thuộc cơ số 16.")
        print(f"Giá trị cơ số 10: {chuyen_co_so_16_sang_10(chuoi)}")
    else:
        print(f"Chuỗi '{chuoi}' không thuộc cơ số 2, 8, hoặc 16.")

