str=input("Nhập chuỗi ký tự: ")
dem=0
for c in str:
    if not('a' <= c.lower() <= 'z' or '0' <= c <='9'):
        dem+=1
print("Số lượng ky tự không phải chữ cái tiếng Anh và không là số trong chuỗi là: ",dem)
