hex = set('0123456789ABCDEF')
str = input("Nhập chuỗi hệ Hex: ")
if all(c.upper() in hex for c in str):
    n = int(str, 16)
    print(f"Số thập phân tương ứng: {n}")
else:
    a = ''.join(c.upper() for c in str if c.upper() in hex)
    n = int(a, 16)
    print(f"Số thập phân tương ứng sau loại bỏ ký tự không thuộc hệ Hex: {n}")
