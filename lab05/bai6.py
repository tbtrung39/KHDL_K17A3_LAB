Str = input("Nhập chuỗi: ")

if all(c in '0123456789ABCDEF' for c in Str.upper()):
    print("Chuỗi là hệ Hex.")
else:
    Str = ''.join(c for c in Str if c in '0123456789ABCDEF')
    decimal = int(Str, 16)
    print("Chuỗi sau khi loại bỏ các ký tự không thuộc hệ Hex và chuyển sang số thập phân: ", decimal)