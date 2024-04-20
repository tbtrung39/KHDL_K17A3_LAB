n = set()
while True:
    a = input("Nhập một ký tự (ấn ESC để kết thúc): ")
    if a == '\x1b':  
        break
    if not a.isdigit():
        n.add(a)
print("Tập hợp sau khi loại bỏ các ký tự số:", n)