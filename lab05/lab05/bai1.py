chuoi = input("nhập chuỗi: ")
count = 0 
for char in chuoi:
    if char.isdigit():  
        count += 1
print("số các kí tự là số trong chuỗi là:",count)