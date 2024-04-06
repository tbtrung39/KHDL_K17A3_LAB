str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")
do_dai_cd = 0  
chuoi_cd = ''  
for i in range(len(str1)):
    for j in range(len(str2)):
        do_dai = 0  
        chuoi = ''  
        while i + do_dai < len(str1) and j + do_dai < len(str2) and str1[i + do_dai] == str2[j + do_dai]:
            chuoi += str1[i + do_dai]  
            do_dai += 1  
        if do_dai > do_dai_cd:
            do_dai_cd = do_dai
            chuoi_cd = chuoi
print(f"Chuỗi ký tự con chung có độ dài cực đại: {chuoi_cd}")