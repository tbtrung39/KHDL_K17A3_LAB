s = int(input("Nhập giây: "))
m = int(input("Nhập phút: "))
h = int(input("Nhập giờ: "))
d = int(input("Nhập ngày: "))
phut_moi = (s//60)
s = (s%60)
m = m + phut_moi
gio_moi = (m//60)
m = (m%60)
h = h + gio_moi
ngay_moi = (h//24)
h = (h%24)
d = d + ngay_moi

print(d,"ngày",h,"giờ",m,"phút",s,"giây")