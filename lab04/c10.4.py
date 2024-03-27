number = (input("Nhập vào một số thập phân: "))
isFloat = False
try:
    float(number)
    isFloat = True
except ValueError:
    isFloat = False
    
while isFloat == False:
    number = (input("Đây không phải số thập phân, vui lòng nhập lại: "))
    try:
        float(number)
        isFloat = True
    except ValueError:
        isFloat = False
        
number_str = str(number)
for char in number_str:
    if char.isdigit():
        if char == '0':
            print("không ", end=" ")
        elif char == '1':
            print("một", end=" ")
        elif char == '2':
            print("hai", end=" ")
        elif char == '3':
            print("ba", end=" ")
        elif char == '4':
            print("bốn", end=" ")
        elif char == '5':
            print("năm", end=" ")
        elif char == '6':
            print("sáu", end=" ")
        elif char == '7':
            print("bảy", end=" ")
        elif char == '8':
            print("tám", end=" ")
        elif char == '9':
            print("chín", end=" ")
print()            
    