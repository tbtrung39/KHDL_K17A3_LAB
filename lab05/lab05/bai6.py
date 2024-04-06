chuoi_nhap = input("Nhập chuỗi: ")

chuoi_nhap = chuoi_nhap.upper()
la_hex = all(ky_tu in "0123456789ABCDEF" for ky_tu in chuoi_nhap)
if la_hex:
    print("Chuỗi này là chuỗi hệ Hex.")
else:
    hex_chars = "0123456789ABCDEF"
    chuoi_loc = ''.join(ky_tu for ky_tu in chuoi_nhap if ky_tu in hex_chars)
    so_thap_phan = int(chuoi_loc, 16)
    print("Chuỗi sau khi loại bỏ các ký tự không thuộc hệ Hex và chuyển sang số thập phân:", so_thap_phan)