str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")
result = ''
len_str1 = len(str1)
len_str2 = len(str2)
i = 0
j = 0

while i < len_str1 and j < len_str2:
    result += str1[i]+str2[j]
    i += 1
    j += 1

result += str1[i:]
result += str2[j:]

print("Chuỗi sau khi trộn:",result)