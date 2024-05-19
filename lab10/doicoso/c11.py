import doicoso1
import doicoso2
n = int(input("Nhập số: "))
print(doicoso1.convert_number_to_binary(n), "là hệ nhị phân của", n)
print(doicoso1.convert_number_to_octal(n), "là hệ bát phân của", n)
print(doicoso1.convert_number_to_hexadecimal(n), "là hệ thập lục phân của", n)

str = input("Nhập chuỗi: ")
number = input("Nhập số: ")
print(doicoso2.syntax_check(str), "là chuỗi cuối cùng")
print(doicoso2.base_number_check(number))
binary = input("Nhập số nhị phân: ")
print(doicoso2.convert_binary_to_decimal(binary), "là hệ thập phân chuyển từ hệ nhị phân")
octal = input("Nhập số bát phân: ")
print(doicoso2.convert_octal_to_decimal(octal), "là hệ thập phân chuyển từ hệ bát phân")
hexa = input("Nhập số thập lục phân: ")
print(doicoso2.convert_hexadecimal_to_decimal(hexa), "là hệ thập phân được chuyển từ hệ thập lục phân")
