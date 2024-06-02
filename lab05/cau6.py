string = input("Nhập chuỗi: ")

is_hex = True
for char in string:
    if char not in "0123456789ABCDEF":
        is_hex = False
        break

if is_hex:
    decimal = int(string, 16)
    print(f"Chuỗi là chuỗi Hex, số thập phân tương ứng là: {decimal}")
else:
    new_string = ""
    for char in string:
        if char in "0123456789ABCDEF":
            new_string += char
    decimal = int(new_string, 16)
    print(f"Chuỗi không phải là chuỗi Hex, số thập phân tương ứng là: {decimal}")