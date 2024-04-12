str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")

result = ''
len1, len2 = len(str1), len(str2)
i, j = 0, 0

while i < len1 and j < len2:
    result += str1[i] + str2[j]
    i += 1
    j += 1

# Nếu một trong hai chuỗi kết thúc, chỉ viết ra các ký tự của chuỗi còn lại
if i < len1:
    result += str1[i:]
if j < len2:
    result += str2[j:]

# In kết quả
print("Chuỗi sau khi trộn:", result)