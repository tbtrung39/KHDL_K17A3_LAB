str1 = input("nhap chuoi ky tu str1:")
str2 =input("nhap chuoi ky tu str2 :")
len1 = len(str1)
len2 = len(str2)
max_length = 0
end_index = 0
for i in range(len1):
    for j in range(len2):
        k=0
        while (i*k < len1 and j+k<len2 and str1[i+k]==str2[j+k]):
            k += 1
        if k >max_length:
            max_length = k
            end_index = i
chuoi_con_chung = str1[end_index - max_length +1 : end_index+1]
if chuoi_con_chung:
    print("chuoi ky tu con chung co do dai cuc dai la :", chuoi_con_chung)
    print("khong co chuoi ky tu con chung")
        
