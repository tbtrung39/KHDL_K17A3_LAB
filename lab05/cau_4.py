str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")
chuoi_tron = ''
i = 0
j = 0
while i < len(str1) and j < len(str2):
    chuoi_tron += str1[i]
    chuoi_tron += str2[j]
    i += 1
    j += 1
chuoi_tron += str1[i:]
chuoi_tron += str2[j:]
print("Chuỗi sau khi trộn là: ", chuoi_tron)
