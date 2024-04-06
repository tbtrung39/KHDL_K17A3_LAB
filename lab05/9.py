
chuoi=input("Nhập chuỗi ký tự: ")
chuoi_con_max = " "
chuoi_con_hien_tai=" "
ky_tu_truoc= ' '
for ky_tu in chuoi:
    if ky_tu == ky_tu_truoc:
        chuoi_con_hien_tai+=ky_tu
    else:
        chuoi_con_hien_tai=ky_tu
    if len(chuoi_con_hien_tai)>len(chuoi_con_max):
        chuoi_con_max=chuoi_con_hien_tai
    ky_tu_truoc=ky_tu
print("Chuỗi con có độ dài cực đại và chỉ chứa các ký tự giống nhau là:", chuoi_con_max)
