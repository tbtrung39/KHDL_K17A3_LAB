# Có bao nhiêu kí tự không phải là chữ cái và số 
Str = input("Nhập một chuỗi kí tự: ")
dem = 0
for i in Str:
    if not i.isalpha() and not i.isdigit():
        dem +=1

print("Số kí tự không phải là chữ cái hay là số là: ", dem)