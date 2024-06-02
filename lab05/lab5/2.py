str= input('Nhập chuỗi ký tự: ')
a = 0
for i in str:
    if i.isalpha():
        a+=1
print(f'Số các chữ cái tiếng anh trong chuỗi là: {a}')