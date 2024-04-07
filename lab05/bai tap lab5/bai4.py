# Trộn chuỗi xâu kí tự
string1 = "Thế giới quả là rộng lớn"
string2 = "Và có rất nhiều việc cần phải làm"

# Độ dài của chuỗi 1 và chuỗi 2
len1 = len(string1)
len2 = len(string2)

# Tìm chiều dài nhỏ nhất của hai chuỗi
min_len = min(len1, len2)

ket_qua = " "

# Trộn các kí tự từ cả hai chuỗi cho đến khi một trong hai chuỗi đã kết thúc
for i in range(min_len):
    ket_qua += string1[i] + string2[i]

# Nếu chuỗi 1 dài hơn chuỗi 2
if len1 > len2:
    ket_qua += string1[min_len:]
# Nếu chuỗi 2 dài hơn chuỗi 1
elif len2 > len1:
    ket_qua += string2[min_len:]

print("Chuỗi kết quả sau khi trộn:", ket_qua)
