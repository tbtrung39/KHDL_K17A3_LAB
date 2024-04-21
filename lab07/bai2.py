numbers = []
num = input("Nhập vào một số tự nhiên (Nhập dấu '.' để kết thúc): ")
while num != ".":
    try:
        num_int = int(num)  
        if num_int >= 0:  
            numbers.append(num_int)
        else:
            print("Giá trị không hợp lệ, vui lòng nhập một số tự nhiên.")
    except ValueError:  
        print("Đây không phải là số tự nhiên, vui lòng nhập lại.")
    
    num = input("Nhập vào một số tự nhiên (Nhập dấu '.' để kết thúc): ")

# Tạo tập hợp từ danh sách
A = set(numbers)
print("Tập hợp A là:", A)
