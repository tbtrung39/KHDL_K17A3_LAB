s = set()
print("Nhập các ký tự. Nhập 'ESC' để kết thúc nhập liệu: ")

while True:
    char = input()
    if char == 'ESC':  
        break
    s.add(char)

s = {i for i in s if not i.isdigit()}

print("Tập hợp sau khi xoá các ký tự số: ", s)
