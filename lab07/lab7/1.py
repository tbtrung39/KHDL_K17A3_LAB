char_set = set()

print("Nhập các ký tự bạn muốn thêm vào set. Nhập 'q' để kết thúc.")

while True:
    char = input()

    if char.lower() == 'q':
        break

    char_set.add(char)

char_set = {char for char in char_set if not char.isdigit()}

print("Set sau khi xóa các ký tự số:", char_set)