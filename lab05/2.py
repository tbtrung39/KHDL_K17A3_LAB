Str = input("Nhập chuỗi ký tự: ")
count = 0

for char in Str:
    if not char.isalpha() and not char.isdigit():
        count += 1

print("Số ký tự không phải là chữ cái tiếng Anh và không là số trong chuỗi là:", count)