
Str = input("Nhập chuỗi: ")
he_hex = '0123456789ABCDEF'
chuoi_hex = ""
he_thap_phan = 0
for i in Str:
    if i.upper() in he_hex:
        chuoi_hex = chuoi_hex + str(i)
        he_thap_phan = he_thap_phan * 16 + int(i, 16)

print("Chuỗi sau khi bỏ các ký tự không thuộc hệ Hex: ", chuoi_hex)
print("Kết quả sau khi chuyển sang hệ thập phân:", he_thap_phan)
