str1 = input("nhap chuoi str1: ")
str2 = input("nhap chuoi str2: ")
chuoi_con_chung = ""

for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        chuoi_con = str1[i:j]
        if chuoi_con in str2 and len(chuoi_con) > len(chuoi_con_chung):
            chuoi_con_chung = chuoi_con

print("Chuoi con chung dai nhat la:", chuoi_con_chung)