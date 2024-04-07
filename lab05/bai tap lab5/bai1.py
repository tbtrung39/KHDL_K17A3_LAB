dem = 0
Str = input("Nhập một chuỗi kí tự: ")
for i in Str:
    if i.isdigit():
        dem+= 1

print("Số các kí tự là số trong chuỗi kí tự Str là:", dem)