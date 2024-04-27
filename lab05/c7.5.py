chuoi = input("Nhập vào một chuỗi: ").lower()
chuoi_moi = ""
for c in chuoi:
    if ("0" <= c <= "9" or ("a" <= c <="f")):
        chuoi_moi +=c
print("Chuỗi trong hệ hex là: ",chuoi_moi.upper())