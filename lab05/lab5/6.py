str = input('Nhập chuỗi : ')
input_str = str.upper()
hex = all(char.isdigit() or (char >= 'A' and char <= 'F') for char in input_str)

if not hex:
    hex_str = ''.join(filter(lambda char: char.isdigit() or (char >= 'A' and char <= 'F'), input_str))
    so_tphan = int(hex_str, 16)
    print(f'Chuỗi không phải là chuỗi Hex. Số thập phân tương ứng: {so_tphan}')
else:
    print('Chuỗi là chuỗi Hex.')