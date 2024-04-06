str1=input("Nhập chuỗi ký tự thứ nhất: ")
str2=input("Nhập chuỗi ký tựu thứ hai: ")
min_len=min(len(str1), len(str2))
chuoi_con_chung=" "
for i in range(min_len):
    if str1[i] == str2[i]:
        chuoi_con_chung += str1[i]
    else:
        break
if chuoi_con_chung:
    print("Chuỗi ký tự con chung có độ dài cực đại là: ", chuoi_con_chung)
else:
    print("Không có chuỗi ký tự con chung")
