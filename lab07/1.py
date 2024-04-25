import msvcrt

# Khởi tạo set
s = set()

print("Nhập các ký tự từ bàn phím (nhấn 'esc' để kết thúc):")

while True:
    char = msvcrt.getch().decode('utf-8')
    if char == '\x1b':  # mã ASCII của 'esc' là '\x1b'
        break
    s.add(char)

# Xóa các ký tự số từ set
s = {char for char in s if not char.isdigit()}

print("Set sau khi xóa các ký tự số:", s)
