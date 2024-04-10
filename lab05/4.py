Str1 = input("Nhập chuỗi thứ nhất:")
Str2 = input("Nhập chuỗi thứ hai:")
len1 = len(Str1)
len2 = len(Str2)
tron_str = ''
i = 0
j = 0
while i < len1 or j < len2:
    if i < len1:
        tron_str += Str1[i]
        i += 1
    if j < len2:
        tron_str += Str2[j]
        j += 1
print("Chuỗi sau khi trộn:", tron_str)
