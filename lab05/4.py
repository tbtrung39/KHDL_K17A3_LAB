Str1 = input("Nhập chuỗi Str1: ")
Str2 = input("Nhập chuỗi Str2: ")

len1 = len(Str1)
len2 = len(Str2)

i = 0
j = 0

while i < len1 or j < len2:
    if i < len1:
        print(Str1[i], end="")
        i += 1
    if j < len2:
        print(Str2[j], end="")
        j += 1