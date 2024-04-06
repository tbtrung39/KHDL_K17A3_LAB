str1 = input("nhập chuỗi 1: ")
str2 = input("nhập chuỗi 2: ")
chuỗi_con_chung_dài_nhất = ""

for i in range(len(str1)):
    for j in range(i+1, len(str1)+1):
        chuỗi_con = str1[i:j]
        if chuỗi_con in str2 and len(chuỗi_con) > len(chuỗi_con_chung_dài_nhất):
            chuỗi_con_chung_dài_nhất = chuỗi_con

if chuỗi_con_chung_dài_nhất == "":
    print("Không có biến chung")
else:
    print("Chuỗi con chung có độ dài cực đại là:", chuỗi_con_chung_dài_nhất)
