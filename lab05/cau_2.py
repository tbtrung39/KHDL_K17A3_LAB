Str = input("Nhập chuỗi: ")
dem = 0
for i in Str:
    if not "0" <= i <= "9" and not i.isalpha():
        dem += 1
print("Số kí tự không phải là chữ cái tiếng Anh và không phải là số trong chuỗi là: ", dem)
