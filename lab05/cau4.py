str1 = input("nhap chuoi str1 :")
str2 = input("nhap chuoi str2 :")
str3 = input("nhap chuoi str3 :")
len1 = len(str1)
len2 = len(str2)
i = 0
j = 0
while i < len1 or j <len2:
    if i < len1:
        print(str1[i], end = "")
        i +=1
        if j < len2:
            print(str2[j], end = "")
        j+=1