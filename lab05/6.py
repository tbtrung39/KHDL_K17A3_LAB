hex_digits = set("0123456789ABCDEF")
Str = input("Nhập chuỗi: ")
hex_str = ''.join(ch for ch in Str.upper() if ch in hex_digits)

if hex_str:
    result = int(hex_str, 16)
    print(f"Chuỗi sau khi loại bỏ các ký tự không thuộc hệ Hex và chuyển sang số thập phân: {result}")
else:
    print("Chuỗi không chứa ký tự thuộc hệ Hex.")
