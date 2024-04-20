my_set = set()
while True:
    char = input('Nhập vào ký tự(Esc để kết thúc): ')
    if char.lower() == 'esc':
        break
    if not char.isdigit():
        my_set.add(char)
print(f'Tập hợp sau khi xóa các ký tự số là: {my_set}')