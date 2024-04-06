str1 = input("Nhập chuỗi Str1: ")
str2 = input("Nhập chuỗi Str2: ")
chuoi_con_chung = ""

for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        chuoi_con = str1[i:j]
        if chuoi_con in str2 and len(chuoi_con) > len(chuoi_con_chung):
            chuoi_con_chung = chuoi_con

print("Chuỗi con chung dài nhất là:", chuoi_con_chung)