chuoi_nhap = input("Nhập chuỗi: ")
hex_digits = set("0123456789ABCDEF")
la_hex = all(ky_tu.upper() in hex_digits for ky_tu in chuoi_nhap)
if la_hex:
    print("Chuỗi đã nhập là chuỗi Hex.")
    gia_tri_thap_phan = int(chuoi_nhap, 16)
    print("Số thập phân tương ứng:", gia_tri_thap_phan)
else:
    print("Chuỗi đã nhập không phải là chuỗi Hex.")
    chuoi_hex_chuan = ''.join(ky_tu.upper() for ky_tu in chuoi_nhap if ky_tu.upper() in hex_digits)
    gia_tri_thap_phan = int(chuoi_hex_chuan, 16)
    print("Chuỗi Hex sau khi loại bỏ ký tự không hợp lệ:", chuoi_hex_chuan)
    print("Số thập phân tương ứng:", gia_tri_thap_phan)
