Str = input("Nhập chuỗi ký tự:")
a = 0
for i in Str:
    if i.isalpha():
        a += 1
print("Số các chữ cái Tiếng Anh trong chuỗi:", a)
