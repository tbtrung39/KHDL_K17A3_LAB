
input_str = input("Nhập chuỗi Str: ")
input_str = input_str.upper()
is_hex = all(char.isdigit() or (char >= 'A' and char <= 'F') for char in input_str)

if not is_hex:
    hex_str = ''.join(filter(lambda char: char.isdigit() or (char >= 'A' and char <= 'F'), input_str))
    decimal_num = int(hex_str, 16)
    print("Chuỗi không phải là chuỗi Hex. Số thập phân tương ứng:", decimal_num)
else:
    print("Chuỗi là chuỗi Hex.")
