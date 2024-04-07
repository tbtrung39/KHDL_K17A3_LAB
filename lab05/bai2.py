chuoi = input("Nhập vào một chuỗi: ").lower()
dem = 0
for c in chuoi:
    if not (("a" <= c <= "z") or ("0" <= c <= "9") or c != " "):
        dem += 1
print("Số các ký tự không phải là chữ cái tiếng Anh và không phải là số trong chuỗi là:",dem)     