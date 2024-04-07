chuoi = "Khoa, khoa học ứng dụng"
chuoi_thay_the = chuoi.replace(",", " ")
print("Chuỗi thay thế là: ",chuoi_thay_the)
tach_chuoi = chuoi_thay_the.split()

print("Chuỗi",chuoi,"sau khi tách là:")

for i in tach_chuoi:
    print(i)