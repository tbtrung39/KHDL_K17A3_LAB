str = input("Nhập chuỗi: ")
char = ''
char in str
if char.isnumeric() == True or char.upper() in 'ABCDEF':
    print(str, "là chuỗi hệ hex")
else:
    print(str, "không phải hệ hex")
str2 = ''
str2 = ''.join(char for char in str if char.upper() in '0123456789ABCDEF')
print(str2, 'là chuỗi đã chuyển sang hệ thập phân')
