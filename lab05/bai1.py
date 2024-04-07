chuoi = input("Nhập vào một chuỗi: ")
dem = 0
for c in chuoi:
    if "0" <= c <= "9":
        dem += 1
print("Số các ký tự là số trong chuỗi là:",dem)    