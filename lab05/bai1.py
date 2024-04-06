#1. Nhập từ bàn phím một chuỗi ký tự Str. Hãy đếm sô các ký tự là số trong chuỗi ký tự Str và in kết quả ra màn hình.
chuoi = input("nhập chuỗi: ")
count = 0 
for char in chuoi:
    if char.isdigit():  
        count += 1
print("số các kí tự là số trong chuỗi là:",count)
