Str = input("Nhập chuỗi: ")
dem = 0
for i in Str:
    if "0" <= i <= "9":
        dem += 1
print("Số kí tự là số trong chuỗi đã nhập là: ", dem)
