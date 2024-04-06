str1=input("Nhập chuỗi ký tự Str1: ")
str2=input("Nhập chuỗi ký tự Str2: ")
ket_qua=' '
len_str1=len(str1)
len_str2=len(str2)
max_len=max(len_str1, len_str2)
for i in range(max_len):
    if i < len_str1:
        ket_qua+=str1[i]
    if i < len_str2:
        ket_qua+=str2[i]
print("Chuỗi sau khi trộn là:", ket_qua)
