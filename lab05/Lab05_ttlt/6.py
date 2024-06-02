def la_thap_luc_phan(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def chuyen_sang_thap_phan(s):
    s = ''.join(filter(lambda x: x in '0123456789ABCDEF', s.upper()))
    return int(s, 16)

Str = input("Nhập chuỗi Str: ")
if la_thap_luc_phan(Str):
    print("Chuỗi Str là chuỗi được viết trong hệ Hexadecimal.")
else:
    gia_tri_thap_phan = chuyen_sang_thap_phan(Str)
    print(f"Chuỗi Str không phải là chuỗi được viết trong hệ Hexadecimal. Giá trị thập phân tương ứng: {gia_tri_thap_phan}")