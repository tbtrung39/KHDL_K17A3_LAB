chuoi_ky_tu = input("Nhập chuỗi ký tự: ")
chuoi_con_max = ""
chuoi_con_hien_tai = ""
for ky_tu in chuoi_ky_tu:
    if ky_tu == chuoi_con_hien_tai[-1:] and chuoi_con_hien_tai:
        chuoi_con_hien_tai += ky_tu
    else:
        chuoi_con_hien_tai = ky_tu
    if len(chuoi_con_hien_tai) > len(chuoi_con_max):
        chuoi_con_max = chuoi_con_hien_tai
print("Chuỗi ký tự con có độ dài cực đại và chứa các ký tự giống nhau là:", chuoi_con_max)
