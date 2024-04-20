ky_tu_set=set()
print("Nhập các ký tự, bấm phím ESC để kết thúc: ")
while True:
    ky_tu=input()
    if ky_tu == "":
        break
    ky_tu_set.add(ky_tu) if not ky_tu.isdigit() else None
print("Set sau khi loại bỏ các ký tự số: ", ky_tu_set)