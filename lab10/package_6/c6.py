import doicoso2
string = input("Nhập chuỗi kí tự: ")
print(doicoso2.syntax_check(string), "là chuỗi cuối cùng")

base_number = int(input("Nhập số: "))
print(doicoso2.base_number_check(base_number))

binary = input("Nhập số nhị phân: ")
print(doicoso2.convert_binary_to_decimal(binary), "là kết quả chuyển sang hệ thập phân")

octal = input("Nhập số bát phân: ")
print(doicoso2.convert_octal_to_decimal(octal), "là kết quả chuyển sang số thập phân")

hexadecimal = input("Nhập số thập lục phân: ")
print(doicoso2.convert_hexadecimal_to_decimal(hexadecimal), "là kết quả chuyển sang số thập phân")