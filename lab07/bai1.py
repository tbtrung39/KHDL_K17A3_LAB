# Set = input("Nhập các kí tự:")
# gia_tri = Set.split(",")
# input_set = set(Set)
# print(input_set)

import msvcrt 
Set = input("Nhập các kí tự:")
gia_tri = Set.split(",")
input_set = set(Set)
print(input_set) 

while True:
    if msvcrt.kbhit():  # Kiểm tra xem có phím nào được nhcấn không
        key = msvcrt.getch()  # Lấy phím được nhấn
        if ord(key) == 27:  # Kiểm tra nếu là phím ESC (mã ASCII của ESC là 27)
            break  # Thoát khỏi vòng lặp khi nhấn ESC

print("Dữ liệu đã nhập:", input_set)
