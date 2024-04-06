
str_input=input("Nhập chuỗi Str: ")
str_input=str_input.upper()
decimal_number=0
for c in str_input:
    if '0' <= c <= '9':
        decimal_number=decimal_number*16+(int(c))
    elif 'A' <= c <= 'F':
        decimal_number = decimal_number*16+(ord(c)-ord('A')+10)
    else:
        decimal_number='j'
        break
print("Số thập phân tương ứng:", decimal_number)
