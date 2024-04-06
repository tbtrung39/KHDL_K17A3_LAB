Str1 = input("Nhập chuỗi thứ nhất: ")
Str2 = input("Nhập chuỗi thứ hai: ")
len1 = len(Str1)
len2 = len(Str2)
max_length = 0
end_index = 0

for i in range(len1):
    for j in range(len2):
        length = 0
        while (i + length < len1) and (j + length < len2) and (Str1[i + length] == Str2[j + length]):
            length += 1
        if length > max_length:
            max_length = length
            end_index = i

chuoi_chung = Str1[end_index:end_index + max_length]
print("Chuỗi con chung có độ dài cực đại:", chuoi_chung)
