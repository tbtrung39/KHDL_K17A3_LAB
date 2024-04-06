#2. Cho trước (hoặc nhập từ bàn phím) chuỗi ký tự Str, có bao nhiêu ký tự không phải là chữ cái tiếng Anh và không là số trong chuỗi Str.
chuoi = input("nhập chuỗi: ")
count = 0 
for char in chuoi:
     if not char.isalpha() and not char.isdigit():
        count += 1
print("số kí tự không phải là chữ cái tiếng Anh và không là số trong chuỗi là:",count)